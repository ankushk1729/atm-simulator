from schema import And, Regex, Schema, SchemaError, Use

user_signup_schema = Schema(
    {
        'full_name': And(Use(str), lambda n : len(n) < 20 ,error = 'Invalid name'),
        'password': Use(str, error = 'Invalid password'),
        'aadhar': And(Use(int), lambda n : len(str(n)) == 12, error = 'Invalid aadhar'),
        'phone':And(Use(int), lambda n : len(str(n)) == 10, error = 'Phone number should be of 10 digits' ),
        'email':And(str, Regex(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'), error = 'Invalid email'),
        'DOB': And(str, Regex(r'^(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.](19|20)\d\d$'), error = 'Invalid date provided')
    }
)

