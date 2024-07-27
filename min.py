def parse_distribution(distribution_type, params):
    try:
        if distribution_type == 'normal':
            mean = params.get('mean', 0)
            stddev = params.get('stddev', 1)
            if stddev <= 0:
                raise ValueError("Standard deviation must be positive")
            distribution = stats.norm(loc=mean, scale=stddev)
        
        elif distribution_type == 'uniform':
            start = params.get('start', 0)
            end = params.get('end', 1)
            if start >= end:
                raise ValueError("End must be greater than start")
            distribution = stats.uniform(loc=start, scale=end-start)
        
        elif distribution_type == 'exponential':
            rate = params.get('rate', 1)
            if rate <= 0:
                raise ValueError("Rate must be positive")
            distribution = stats.expon(scale=1/rate)
        
        else:
            raise ValueError(f"Unsupported distribution type: {distribution_type}")
        
        return distribution
    
    except Exception as e:
        print(f"Error parsing {distribution_type} distribution parameters: {e}")
        return None

# Example usage
dist_params = {
    'mean': 5,
    'stddev': 1
}
normal_dist = parse_distribution('normal', dist_params)

if normal_dist:
    print("Normal distribution created successfully")
    print(f"Mean: {normal_dist.mean()}, StdDev: {normal_dist.std()}")
else:
    print("Failed to create normal distribution")
