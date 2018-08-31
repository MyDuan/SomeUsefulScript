for __PID in $(ps -ef | grep -F 'sudo -u nn -i ssh <your server>' | awk '{ print $2}'); 
do 
  if [ $(basename $(readlink -esn /proc/${__PID}/cwd) 2>/dev/null || echo '?') = <username> ]; 
  then 
    echo ${__PID}; 
  fi; 
done
