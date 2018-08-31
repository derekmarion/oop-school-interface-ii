require_relative 'person'

class Student < Person
    attr_reader :school_id

    def initialize(args)
        super
       @school_id = args.fetch(:school_id)
    end 

    def self.all
        CSV.foreach('./data/students.csv', headers: true, header_converters: :symbol ).map do |student_info|
            Student.new(student_info.to_h)
        end 
    end 
end 