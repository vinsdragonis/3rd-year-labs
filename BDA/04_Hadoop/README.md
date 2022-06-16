    start-all.sh      (type password)

    jps         (5604 DataNode
    5415 NameNode
    5815 SecondaryNameNode
    6471 Jps
    5977 ResourceManager
    6300 NodeManager
    )


    1.MKDIR create directory
    hdfs dfs -mkdir /Test

    2.LS command
    hdfs dfs -ls /Test


    3.PUT command
    hdfs dfs -put /home/hduser/Desktop/goodbye.txt    /Test
    hdfs dfs -cat /Test/goodbye.txt                              (hdfs dfs -cat for hadoop file system)

    7.CAT
    hdfs dfs -cat /Test/goodbye.txt  

    4.COPYFROMLOCAL 
    hdfs dfs -copyFromLocal /home/hduser/Desktop/Welcome.txt     /Test
    hdfs dfs -cat /Test/Welcome.txt         //

    5.GET
    i)hdfs dfs -get /Test/goodbye.txt     /home/hduser/Desktop/goodbye1.txt
      cat /home/hduser/Desktop/goodbye1.txt       (just cat for local file)

    ii)hdfs dfs -getmerge   /Test/Welcome.txt    /Test/goodbye.txt     /home/hduser/Desktop/Merge.txt
       cat /home/hduser/Desktop/Merge.txt

    iii)hdfs dfs -getfacl /Test             (or use– hadoop fs)

    Output—
    # file: /Test
    # owner: hduser
    # group: supergroup
    user::rwx
    group::r-x
    other::r-x


    6.COPYTOLOCAL
    hdfs dfs -copyToLocal /Test/goodbye.txt /home/hduser/Desktop/New.txt
    cat /home/hduser/Desktop/New.txt


    8.MV
    hdfs dfs -mkdir /Test2
    hdfs dfs -mv /Test /Test2
    hdfs dfs -ls /Test           // ls: `/Test': No such file or directory
    hdfs dfs -ls /Test2         // Found 1 items
     drwxr-xr-x   - hduser supergroup          0 2022-06-06 12:05 /Test2/Test

    9. CP
    hdfs dfs -mkdir /Test3
    hdfs dfs -cp /Test2 /Test3
    hdfs dfs -ls /Test3              // Found 1 items
    drwxr-xr-x   - hduser supergroup          0 2022-06-06 12:32 /Test3/Test2


    hdfs dfs -ls /Test2      //Found 1 items
    drwxr-xr-x   - hduser supergroup          0 2022-06-06 12:05 /Test2/Test
