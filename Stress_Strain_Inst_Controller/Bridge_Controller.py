import pyvisa

class Instrument:
    @staticmethod
    def list_inst():
        resource_manager = pyvisa.ResourceManager()
        return resource_manager.list_resources()
    
    def __init__(self, address):
        resource_manager = pyvisa.ResourceManager()

        termination_char = "\n"
        self._instrument = resource_manager.open_resource(address, read_termination = termination_char)

    def IDN(self):
        return self._instrument.query(r'*IDN?')

class AH_Bridge(Instrument):
    def single(self):
        return self._instrument.query(r'SINGLE')
    def continuous(self):
        return self._instrument.query(r'CONTINUOUS') #I'm not sure how this one will work. Do we need to regularly read?

class VoltSource(Instrument):
    #It seems that most of the commands can be abberivated.
    #I found the proper manual: Check all the commands are correct.
    def __init__(self, address):
        super().__init__(address)
        self.set_vmode()
    def set_vmode(self):
        return self.set_vmode(r":SOURce[1]:FUNCtion[:MODE] VOLTage")
    def set_fixed(self):
        return self._instrument.write(r":SOURce[1]:VOLTage:MODE FIXed")
    def set_volt_limit(self, limit):
        command = r":SOURce[1]:VOLTage:PROTection[:LEVel] PROT"
        return self._instrument.write(f"{command}{limit}")
    def get_volt_limit(self):
        return self._instrument.query(r":SOURce[1]:VOLTage:PROTection[:LIMit]?")
    def set_curr_limit(self, limit):
        command = r":SOURce[1]:VOLTage:ILIMit[:LEVel]"
        self._instrument.write(f"{command} {limit}") #ILIM
    def get_curr_limit(self):
        return self._instrument.query(r":SOURce[1]:VOLTage:ILIMit[:LEVel]")
    def set_volt(self, V):
        #It may be worth adding a unit prefix requirement to V.
        command = r":SOURce[1]:VOLTage[:LEVel][:IMMediate][:AMPLitude]"
        return self._instrument.write(f"{command} {V}")
    def get_volt(self):
        return self._instrument.query(r":SOURce[1]:VOLTage[:LEVel][:IMMediate][:AMPLitude]?")
     

    
