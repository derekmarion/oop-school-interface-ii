require 'csv'

class Person 
    attr_reader :name, :password, :age, :role

    def initialize(args)
        @name = args.fetch(:name)
        @age = args.fetch(:age)
        @password = args.fetch(:password)
        @role = args.fetch(:role)
    end 
end 