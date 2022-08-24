from schema import And, Schema, Use

user_schema = Schema(
    {
        'full_name': And(Use(str), lambda n : len(n) < 20 ,error = 'Invalid name'),
        'password': Use(str, error = 'Invalid password'),
        'aadhar': Use(int, error = 'Invalid aadhar'),
        'phone':And(Use(int), lambda n : len(str(n)) == 10 ),
        'email':Use(str) # Will add regex validation for email
    }
)

















# def func():
#     validated = user_schema.validate({
#     'full_name':'dsbaaaaaaaaa',
#     'password':'hello',
#     'aadhar':123344444
# })
