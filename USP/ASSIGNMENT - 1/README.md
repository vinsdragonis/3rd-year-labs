# USP Assignment - 1
## Date: 20th December 2021

1. Describe the methods to  change the file permissions with examples.
   
   We can change file permissions using `chmod` command.<br />
   The general syntax for **`chmod`** is:<br />
   
        chmod [reference][operator][MODE] file...
      
   There are **2 ways** to define file permissions:
  
      a. **Absolute method**: We can *replace* the existing permissions.<br />
        **Example**:

              chmod 777 fname.sh

      b. **Relative method**: We can *modify* the existing permissions.<br />
        **Example**:

              chmod u+rwx fname.sh

##

2. Bring out the differences between **hard links** and **soft links** with an example.
    <br />

    <table>
        <tr>
            <th><strong>Criteria</strong></th>
            <th><strong>Hard Links</strong></th>
            <th><strong>Soft Links</strong></th>
        </tr>
        <tr>
            <td>Inode number</td>
            <td>Files which are hard linked have same inode number</td>
            <td>Files which are soft linked have different inode number</td>
        </tr>
        <tr>
            <td>File systems</td>
            <td>Hard links can't be used across file systems</td>
            <td>Soft links can be used across file systems</td>
        </tr>
        <tr>
            <td>Directories</td>
            <td>Hard links are not allowed for directories</td>
            <td>Soft links can be used to link directories</td>
        </tr>
        <tr>
            <td>Speed</td>
            <td>Hard linked are relatively faster</td>
            <td>Soft linked are relatively slower</td>
        </tr>
    </table>

##

3. Use find command to locate from home directory:
    1. All files having inode number 9076
    2. All directories having permissions 666
    3. All files not accessed for more than a year
    4. All but C program files
    <br />
    
    1. `find / -inum 9076 -print`
    2. `find / -perm 666 -print`
    3. `find / -atime +60 -type f -print`
    4. `find / -name ".c" -print`
