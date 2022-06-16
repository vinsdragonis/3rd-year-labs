1. Start mongo shell

        mongo

2. Create new database

        use student;

3. Show databases list

        show dbs;

4. Create new collection

        db.createCollection("students");
        
5. Insert single record

        db.student.insert(
            {
                _id:1,
                Name:"Vineeth",
                USN:"1BM19CS033",
                Sem:6,
                Dept:'CSE',
                CGPA:7.8,
                hobbies:["Skating","Gaming","Coding","Watch anime"]
            }
        );

5. Insert multiple records

        var myStudents = [
            {
                _id:2,
                Name:"Jahnavi",
                USN:"1BM19CS065",
                Sem:6,
                Dept:'CSE',
                CGPA:9.8,
                hobbies:["Coding","Watch TV","Play throwball"]
            },
            {
                _id:3,
                Name:"Derek",
                USN:"1BM19CS045",
                Sem:6,
                Dept:'CSE',
                CGPA:9.3,
                hobbies:["Read novels","Watch anime","Gaming"]
            },
            {
                _id:4,
                Name:"Samarth",
                USN:"1BM19CS141",
                Sem:6,
                Dept:'CSE',
                CGPA:7.5,
                hobbies:["Daydream","Gaming","Watch anime"]
            }
        ];
        
        db.student.insert(myStudents);

6. List all documents
        
        db.student.find({});

7. Find record

        db.student.find({Name:"Vineeth"});
        db.student.find({},{_id:1});

8. Update record

        db.student.update({_id:4},{$set:{USN:"1BM19CS141"});

9. Import CSV file

        mongoimport --db student --collection students --type csv --headerline --file /home/output.csv

10. Export to CSV

        mongoexport --host localhost --db student --collection student --type=csv --out  output.csv --fields "USN","semester","Name","dept_name"
