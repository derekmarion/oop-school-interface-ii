require_relative 'person'

class Staff < Person
    attr_reader :employee_id

    def initialize(args)
        super
        @employee_id = args.fetch(:employee_id)
    end 

    def self.all
        CSV.foreach('./data/staff.csv', headers: true, header_converters: :symbol ).map do |staff_info|
            Staff.new(staff_info.to_h)
        end 
    end 
end 
