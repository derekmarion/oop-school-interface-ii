# School Interface Two

## Release 0: Menu

Let's think about our program from the user's point of view for a moment. The first thing we want them to see when the program starts is a menu that lists all the actions they can take. 

```
What would you like to do?
Options:
    1. List All Students
    2. View Individual  Student <student_id>
    3. Add a Student
    4. Remove a Student <student_id>
    5. Quit
```
Let's create our menu first and then we can work down the list and implement each feature one at a time.  

We'll start by putting this logic in our runner file. We can always pull it out later if need be. 

Replace the lines that are printing out the `staff` and `student` variables with this code for the menu. 

```Ruby
#runner.rb 

    puts "\nWhat would you like to do?\nOptions:\n1. List All Students\n2. View Individual Student <student_id>\n3. Add a Student\n4. Remove a Student <student_id>\n5. Quit"

```
The above code might look strange, but when we run it we'll find that our menu prints out just the way we want it to. The `\n` in the string tells ruby to start a new line.  

Right now we have a program that prints a menu and then exits. That's not very useful. We want to give the user the option to select one of the menu items. We can do that using `gets.chomp`. 

```Ruby
#runner.rb 

    puts "\nWhat would you like to do?\nOptions:\n1. List All Students\n2. View Individual Student <student_id>\n3. Add a Student\n4. Remove a Student <student_id>\n5. Quit"

    mode = gets.chomp 

```

We are going to have our user choose options by their number. If they enter `1` we'll list all students, if they enter `2` they can view a specific student's info etc. We'll worry about error handling later. 

Let's make another design decision here. We could handle user input with a series of if statements. That would be perfectly valid. But there's another type of conditional in `Ruby` called a [case statment](http://www.rubyguides.com/2015/10/ruby-case/) that will work nicely for us here. 

If this makes you nervous feel free to just use an if statement, but we'll go ahead with a case statement for now. We'll build it out as we go. Let's just start with what happens when `mode == '1'`

```Ruby
#runner.rb 

    mode = gets.chomp 
    # throwing this puts in here just to give us a space to keep things a little clearer 
    puts '' 
    case mode 
    when '1'
        school.list_students
    else 
        return 
    end  
```
Right now if the user enters a `'1'` our program will run the the `list_students` method on our school object. Any other input will return and exit the program. Run `ruby runner.rb` and enter `'1'`. You'll get an error. What does it say? 

In `school.rb` write a method `list_students` that prints out a numbered list of student names followed by their school_ids. You're output should look something like this: 

```
1. Lisa 13345
2. Jessie 12335
3. Slater 12645
4. kim 34456
5. dave 788908
6. doug 0809890
```

## Release 1: View Single Student 

Next let's give the user the ability to see data about a single student. First, we'll update our case statement. 

```Ruby
case mode 
when '1'
    school.list_students
when '2'
    puts 'Enter student id:'
    puts school.find_student_by_id(gets.chomp) 
else 
    return 
end  
```
After the user chooses to view a student, they'll have to enter a student id so we have a way to look up the student. This is better than searching by name because there can be several students with the same name, but ideally each student will have a unique id. 

We could save the result of `gets.chomp` to a variable, but since that variable is going to go directly into our method, we can skip it here and just call `gets.chomp` as our argument. 

Again if we run this and choose `'2'` we will get an error because we haven't written the method yet. 

In `school.rb` define a method `find_student_by_id` that takes in an id and returns the student with the matching id. If it doesn't find anything it returns nil. 

When you're done you should be able to run `ruby runner.rb`, enter `'2'` and have the student object print out in the terminal. It'll look ugly, but we'll handle that in the next release. 

## Release 2: The to_s Method

You may have noticed that we've been using `puts` to print output instead of `p`. `puts` does two things for us that `p` does not. First, it calls `to_s` on what we pass it (if that object has a `to_s` method defined). It also adds an extra line at the end, which helps us keep our output clean. [Read more about puts, p, and print here.](https://www.garethrees.co.uk/2013/05/04/p-vs-puts-vs-print-in-ruby/)

`to_s` is a `Ruby` method that converts an object into a string. It literally stands for 'to string'. Some objects have a `to_s` method defined already. For objects we make ourselves (like our student class) we can define our own `to_s` method that will automatically get called when we use `puts`. 

Let's do that for our student class now. 

```Ruby
def to_s
    "\n#{name.upcase}\n---------------\nage: #{age}\nid: #{school_id}\n"
end
```
Our student class doesn't really have much going on right now, but you can see that if we wanted to add more info (address, phone number, dob etc) we'd want it all to print out in a way that was easily readable. 

Now run `ruby runner.rb` and select '2'. The output should look something like this. 

```
LISA
---------------
age: 25
id: 13345
```

## Release 3: Quit

We've implemented two of or our features. One problem we can fix before we're done for today is the fact that our program quits out after one action. We want the user to be able to view multiple students in a session. How can we use a loop to include this functionality? Add code to `runner.rb` so that after showing the list of students or the data from a single student, the menu displays again and the user can input another selection. Only when the user inputs a `'5'` should the program exit. 

