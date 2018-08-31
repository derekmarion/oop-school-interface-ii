require_relative 'student'
require_relative 'staff'

class School
    attr_reader :name, :students, :staff

    def initialize(name, address = nil)
        @name = name 
        @address = address   
        @students = Student.all
        @staff = Staff.all  
    end   
end 

