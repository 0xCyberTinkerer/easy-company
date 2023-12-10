from pymem import *
from pymem.process import *
#from graph import janela #para quando a interface gráfica estiver pronta

pm = pymem.Pymem("#####.exe")

gameModule = module_from_name(pm.process_handle, "#####.dll").lpBaseOfDll

def GetPtrAddr(base, offsets):
    addr = pm.read_longlong(base)
    for i in offsets:
        if i !=offsets[-1]:
            addr = pm.read_longlong(addr + i)
    return addr + offsets[-1]

while True:
    #pm.write_int(GetPtrAddr(gameModule + 0x01BE9D00, [0x1A8, 0x198, 0x1B8, 0xB0, 0x1F4]), 2000)#dinheiro
    #pm.write_float(GetPtrAddr(gameModule + 0x01CCC2D8, [0xD0, 0x8, 0x68, 0x10, 0xF8, 0x418]), 4.99999905)#velocidade default=4.99999905
    #pm.write_float(GetPtrAddr(gameModule + 0x01CCC2D8, [0xD0, 0x8, 0x68, 0x10, 0xF8, 0x440]), 1.)#stamina default 1.
    #pm.write_int(GetPtrAddr(gameModule + 0x01CCC2D8, [0xD0, 0x8, 0x68, 0x10, 0xF8, 0x59C]), 100) #vida default 100.
    #pm.write_int(GetPtrAddr(gameModule + 0x01CCC2D8, [0xD0, 0x8, 0x68, 0x10, 0xF8, 0x5DC]), 3) #throw default 3. Não funciona
