# Example code to demonstrate basic usage of TurboMemory X

from turbomemory import System

# Initialize the system
system = System()

# Configure FPGA
system.configure_fpga(fpga_config_file='config/fpga_config.bit')

# Configure DDR
system.configure_ddr(ddr_config_file='config/ddr_config.json')

# Start data processing
system.start_processing()

print("System is running...")
