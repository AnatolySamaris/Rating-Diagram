# Rating-Diagram

It's my first lab work on the university course "Computer Graphics", so the task was to draw some simple diagram using some data from a text file.

...But I thought it can be better, and here we now.

The program stores data in CSV format. An object here is only two elements: group and grade of a student.

Here I created 4 groups for each year of a bachelor's program "Applied Mathematics" in my university (btw, I'm studying on this program),
and here we can add a hypothetical student of some of these groups and his average learning score and watch a distribution of average scores in
one of the groups.

The program does not mean a lot, I just wanted to try new lib DearPyGui and create something pretty and have a work, that is better than others in
my group.

## Examples
-------------------------

Initial state. Here we can immediately see AM-19 group diagram:
![image](https://user-images.githubusercontent.com/92950839/216827550-fec6283c-f9e7-4b89-902c-c3ded4b82df3.png)

Adding a new student. If there's no mistakes in the input, we get a message "Added" on the right side of the button:
![image](https://user-images.githubusercontent.com/92950839/216827729-df0f0881-ce3b-4ed5-891a-f0f677fcdbdc.png)

If we try to add a student from other group, nothing but a warning happens:
![image](https://user-images.githubusercontent.com/92950839/216827778-838d9fbc-23a1-4b07-8389-93ebd5c4e936.png)

And also if we try to get better rating...
![image](https://user-images.githubusercontent.com/92950839/216827805-bbe46db8-1d0f-498b-be52-826308592ec4.png)

The group "AM-20" was left empty on purpose, here we can "create" a group rating from scratch. But now there's no students from AM-20,
and we have this:
![image](https://user-images.githubusercontent.com/92950839/216827919-34d90101-2d26-4e3a-933b-161c7e1262c1.png)


### That's all! Thanks for reading!
