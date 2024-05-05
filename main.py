import numpy as np

class ResourceAllocator:
    def __init__(self, max_servers):
        self.max_servers = max_servers
        self.current_servers = 0
    
    def allocate_resources(self, user_traffic, course_popularity, system_load):
        # Calculate desired number of servers based on factors
        desired_servers = self.calculate_desired_servers(user_traffic, course_popularity, system_load)
        
        # Update number of servers
        self.adjust_servers(desired_servers)
        
        return self.current_servers
    
    def calculate_desired_servers(self, user_traffic, course_popularity, system_load):
        # Example: Desired servers proportional to user traffic and course popularity, inversely proportional to system load
        desired_servers = user_traffic * course_popularity / system_load
        
        # Ensure desired servers stay within bounds
        desired_servers = min(max(desired_servers, 0), self.max_servers)
        
        return desired_servers
    
    def adjust_servers(self, desired_servers):
        # Adjust number of servers towards desired value
        if desired_servers > self.current_servers:
            self.current_servers = min(self.current_servers + 1, self.max_servers)
        elif desired_servers < self.current_servers:
            self.current_servers = max(self.current_servers - 1, 0)

# Example usage
if __name__ == "__main__":
    # Initialize resource allocator with maximum number of servers
    allocator = ResourceAllocator(max_servers=10)
    
    # Simulate changing conditions
    user_traffic = np.random.randint(1, 100)
    course_popularity = np.random.rand()
    system_load = np.random.rand()
    
    # Allocate resources dynamically
    allocated_servers = allocator.allocate_resources(user_traffic, course_popularity, system_load)
    
    print("Allocated servers:", allocated_servers)
