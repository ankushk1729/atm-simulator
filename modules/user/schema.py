from schema import And, Regex, Schema, SchemaError, Use

user_schema = Schema(
    {
        'full_name': And(Use(str), lambda n : len(n) < 20 ,error = 'Invalid name'),
        'password': Use(str, error = 'Invalid password'),
        'aadhar': Use(int, error = 'Invalid aadhar'),
        'phone':And(Use(int), lambda n : len(str(n)) == 10, error = 'Phone number should be of 10 digits' ),
        'email':And(str, Regex(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'), error = 'Invalid email'),
        'DOB': Use(str)
    }
)
