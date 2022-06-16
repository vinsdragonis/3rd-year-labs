    > use library;
    > create table library_info(
               ... stud_id text,
               ... stud_name text,
               ... book_name text,
               ... book_id text,
               ... date_of_issue text,
               ... counter_value counter,
               ... primary key((stud_id,book_id),stud_name,book_name,date_of_issue)
               ... );

    > desc library_info;
    CREATE TABLE library.library_info (
        stud_id text,
        book_id text,
        stud_name text,
        book_name text,
        date_of_issue text,
        counter_value counter,
        PRIMARY KEY ((stud_id, book_id), stud_name, book_name, date_of_issue)
    ) WITH CLUSTERING ORDER BY (stud_name ASC, book_name ASC, date_of_issue ASC)

    > update library_info set counter_value=counter_value+1 where stud_id='1bm19cs033' and stud_name='Vineeth' and book_name='CNS' and  book_id='uu9990' and date_of_issue='09-08-2020';
    > select * from library_info;

     stud_id    | book_id | stud_name      | book_name       | date_of_issue | counter_value
    ------------+---------+----------------+-----------------+---------------+---------------
     1bm19cs033 |  uu9990 |        Vineeth |             CNS |    09-08-2020 |             1

    (1 rows)

    update library_info set counter_value=counter_value+1 where stud_id='1bm19cs065' and stud_name='Jahnavi' and book_name='ML' and  book_id='u2f9990' and date_of_issue='09-08-2024'; 
    update library_info set counter_value=counter_value+1 where stud_id='1bm19cs045' and stud_name='Derek' and book_name='OOMD' and  book_id='d8v339' and date_of_issue='19-03-2022';
    update library_info set counter_value=counter_value+1 where stud_id='1bm19cs141' and stud_name='Samarth' and book_name='BDA' and  book_id='dvt543' and date_of_issue='17-04-2022';




     select * from library_info;

     stud_id    | book_id | stud_name | book_name                      | date_of_issue | counter_value
    ------------+---------+-----------+--------------------------------+---------------+---------------
     1bm19cs008 | u2f9990 |   Jahnavi |                             ML |    09-08-2024 |             1
     1bm19cs012 |  d8v339 |     Derek |                           OOMD |    19-03-2022 |             1
     1bm19cs022 |  dvt543 |   Samarth |                            BDA |    17-04-2022 |             2
     1bm19cs008 |  uu9990 |   Vineeth |                            CNS |    09-08-2020 |             1

    (4 rows)



    select * from library_info where counter_value=2 and book_name='BDA'  allow filtering;

     stud_id    | book_id | stud_name | book_name | date_of_issue | counter_value
    ------------+---------+-----------+-----------+---------------+---------------
     1bm19cs022 |  dvt543 |   Samarth |       BDA |    17-04-2022 |             2




    --> (export the created column to csv)

    copy library_info(counter_value,stud_id,stud_name,book_name,book_id,data_of_issue) to 'c:\users\desktop\college\bda\lab3\file.csv' WITH HEADER = TRUE;


    --> (import csv file to cassandra from local storage)

    copy library_info_duplicate from 'c:\users\desktop\college\bda\lab3\file.csv' WITH HEADER = TRUE;
