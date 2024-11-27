1. echo Aleks

2. pwd > files/2.txt
    whoami >> files/2.txt

3. ls -la ~ > ~/otchet/files/3.txt

4. cat ~/{4.txt,4.md}
    cat >> 4.txt
    help // ctrl + d
    cat 4.txt > 4.md

5. chmod go-r 4.txt

6. chmod 722 4.txt

7. mv {4.md,4.txt} ~/otchet/files

8. sudo chown -R kornev:root ~/otchet/files/4.md

9. sudo groupadd wheel
    sudo useradd -m -G wheel -s /bin/zsh test_user

10. sudo passwd test_user
    1111

11. //why we need to do this again... ok
    useradd -aG wheel test_user

12. cat /etc/passwd > ~/otchet/files/12.txt

13. chmod a+w ~/otchet/files/12.txt

14. su -P test_user

15. whoami >> ~/otchet/files/12.txt
    pwd >> ~/otchet/files/12.txt
    // but we have no permission;

16. exit

17. sudo su root 

18. cd /home/test_user
    whoami >> /home/kornev/otchet/files/12.txt
    pwd >> /home/kornev/otchet/files/12.txt
    exit

19. tail --lines=2 ~/otchet/files/12.txt

20. userdel -r test_user 

21. find ~ -maxdepth 2 -depth -empty > ~/otchet/files/21.txt

22. sudo find / -maxdepth 3 -user root -name "dev*" > ~/otchet/files/22.txt

23. mkdir ~/test_find/{time,permissons}

24. touch ~/test_find/time/{one.txt,two.txt}
    touch -a -t 202401010000 ~/test_find/time/one.txt
    // ls -lu ~/test_find/time/one.txt
    touch -m 202410140000 ~/test_find/time/two.txt
    // ls -la ~/test_find/time/two.txt

25. touch ~/test_find/permissions/{cant_write.txt,can_execute.txt}
    chmod a-w ~/test_find/permissions/cant_write.txt
    chmod a+x ~/test_find/permissions/can_execute.txt

26. find ~/test_find -atime +183 -empty -exec rm {} \;


27. find ~/test_find -perm 755 -empty -exec chmod a-x {} \;
    // on my skreenshot permission on can_execute.txt was 775

28. man ls > ~/man_ls.txt

29. grep -n "^$" ~/man_ls.txt

30. grep -E -n "[0-9]+" ~/man_ls.txt

31. grep -i -n "author" ~/man_ls.txt

32. wc -l -c ~/man_ls.txt

33. ps aux -u kornev > ~/otchet/files/33.txt

34. //another terminal. nano

35. pgrep nano // id 4513

36. kill -9 4513

37. htop > F6(filter by) > %CPU

38. DONE