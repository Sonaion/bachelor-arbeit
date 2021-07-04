class Computer:
    id = 0

    def __init__(self, cpu, gpu, ram):
        self.cpu = cpu
        self.gpu = gpu
        self.ram = ram
        self.id = Computer.id
        Computer.id += 1

    def __repr__(self):
        return str(self.id)


def function(computer_array):
    if len(computer_array)==0:
        return []
    if "AMD" in computer_array[0].cpu and "NVIDIA GTX30" in computer_array[0].gpu and computer_array[0].ram >= 16:
        return [computer_array[0]] + function(computer_array[1:])
    else:
        return function(computer_array[1:])


computer_array = []
computer_array.append(Computer("INTEL i7-860", "NVIDIA GTX3080", 16))
computer_array.append(Computer("AMD 5900x", "NVIDIA GTX3080", 32))
computer_array.append(Computer("INTEL i9-10900T", "NVIDIA GTX1070", 8))
computer_array.append(Computer("AMD 5900x", "AMD RX6900", 8))
computer_array.append(Computer("AMD 5700", "AMD RX6900", 16))
computer_array.append(Computer("AMD 5900x", "NVIDIA GTX3090", 64))
computer_array.append(Computer("INTEL i5-8400", "NVIDIA GTX1060", 4))
print(function(computer_array))