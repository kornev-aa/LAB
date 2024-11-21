2. tree -d -L 2 ~

3. cd /etc/

4. ls -a /etc/

5. ls -la --sort='extension' ~

6. and 7. in one time: cd ~
   mkdir -p structure/{2018..2023}/{files,pictures,.passwords}

8. cd 2018
   cd files
   touch data.md
   ... with all alse directores

9. // it was a mistake, I'll never do it like this again
   cd structure
   touch {2018..2023}/pictures/picture.png

10. touch {2018..2023}/.passwords/.passwords.txt

11. touch -a -t 202401010000 {2018..2023}/files/data.md
    ls -lu 2018/files    //for cheak is it right

12. touch -m 201806100000 2018/.passwords/.passwords.txt // {2018..2023}

    ls -la 2018/.passwords/.passwords.txt    //for cheak is it right
    // i have a problem that this command cope a modif time to /structure, i have to remove it
13. cp -r ~/structure/2023 ~/Downloads/2025

14. touch -m 202506100000 ~/Downloads/2025/.passwords/.passwords.txt

15. cp Downloads/2025 structure

16. mv -n ~/structure/2025 2024

17. // building wall
    // i have  this error with cope again like image.png in /structure
    mv -n ~/structure/2018/pictures/picture.png image.png
      mv -n ~/structure/2020/pictures/picture.png image.png
       mv -n ~/structure/2021/pictures/picture.png image.png
        mv -n ~/structure/2022/pictures/picture.png image.png
         mv -n ~/structure/2023/pictures/picture.png image.png
          mv -n ~/structure/2024/pictures/picture.png image.png

18. //i print rm ............ biggest mistake ever i made
    mv ~/structure/2018 ~/Documents

19. rmdir Documents/2024 //directore not empty

20. rm -r Documents/2024

21. cat >> ~/structure/2019/files/data.md
    help-me-pls //enter, ctrl+d to save files

22. nano ~/structure/2019/files/data.md
    // ctrl + 0, enter, ctrl + x

23. code ~/structure/2019/files/data.md

24. cat ~/structure/2020/files/data.md > ~/structure/2022/files/data.md

25. mkdir ~/structure/{soft_links,hard_links}

26. ln -s ~/structure/2019 ~/structure/soft_links/2019
    // {2019..2023}

27. ln ~/structure/2020/files/data.md ~/structure/hard_links/data.md
    ln ~/structure/2021/.passwords/.password.md ~/structure/hard_links/passwords.md
    // i have a problem with diferent names of files, idk will u have this error too

28. mkdir ~/structure/archives

29. // download image.png
30. mv ~/Downloads/image.jpg ~/structure/archives

31. tar -c -f image.jpg.tar ~/structure/archives/image.jpg
    tar -c -f image.jpg.tar.gz ~/structure/archives/image.jpg
    tar -c -f image.jpg.tar.gz2 ~/structure/archives/image.jpg

32. zip -r -e ~/structure.zip structure
    password: 1111 