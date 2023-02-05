FROM ubuntu:latest

USER root

ARG USR1NAME="penguinusr"
ARG USR2NAME="alex"
ARG USR3NAME="mumble"

ARG USR1DIR="/home/${USR1NAME}"
ARG USR2DIR="/home/${USR2NAME}"
ARG USR3DIR="/home/${USR3NAME}"
ARG FTPDIR="/ftpfiles"

RUN mkdir -p "${USR1DIR}"
RUN mkdir -p "${USR2DIR}"
RUN mkdir -p "${USR3DIR}"

RUN echo "*** install dependencies ***"
RUN apt-get -qq update -y 
RUN apt-get -qq install -y netcat vsftpd openssh-server supervisor vim
RUN rm -rf /var/lib/apt/* 

RUN echo "*** set config files 1 ***"
COPY confs/vsftpd.conf /etc/vsftpd.conf
COPY confs/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY confs/sshd_config /etc/ssh/sshd_config

RUN echo "*** create challenge users ***"
RUN useradd --no-create-home -s /bin/bash --home-dir "${USR1DIR}" "${USR1NAME}"
RUN useradd --no-create-home -s /bin/bash --home-dir "${USR2DIR}" "${USR2NAME}"
RUN useradd --no-create-home -s /bin/bash --home-dir "${USR3DIR}" "${USR3NAME}"

RUN echo "*** config SSH ***"
RUN echo "${USR1NAME}:UWA{fTpLipP3r5}" | chpasswd
RUN echo "${USR2NAME}:gonnawhackmykeyboardtomakesecure92p8yij37u49723ihuj23esdf" | chpasswd
RUN service ssh start

RUN echo "*** config VSFTPD ***"
RUN mkdir -p "${FTPDIR}"
COPY files/note-to-flipper-pals.txt ${FTPDIR}/note-to-flipper-pals.txt
RUN chmod -R 555 ${FTPDIR}

RUN echo "*** config flag 2 ***"
COPY files/flag2.txt ${USR1DIR}/flag2.txt
RUN chown root:${USR1NAME} ${USR1DIR}/flag2.txt && chmod 440 ${USR1DIR}/flag2.txt

RUN echo "*** config flag 3 ***"
COPY files/fix-passwords.sh /root/fix-passwords.sh
RUN chmod u+x /root/fix-passwords.sh
COPY files/flag3.txt ${USR2DIR}/flag3.txt
RUN chown root:${USR2NAME} ${USR2DIR}/flag3.txt && chmod 440 ${USR2DIR}/flag3.txt

RUN echo "*** config flag 4 ***"
COPY files/note-to-alex.txt ${USR2DIR}/note-to-alex.txt
COPY files/execute-scripts.sh ${USR3DIR}/execute-scripts.sh
RUN chmod +x ${USR3DIR}/execute-scripts.sh
COPY files/flag4.txt ${USR3DIR}/flag4.txt
RUN chown root:mumble ${USR3DIR}/flag4.txt && chmod 440 ${USR3DIR}/flag4.txt
RUN mkdir -p /opt/admin-scripts && chown mumble:alex /opt/admin-scripts && chmod 770 /opt/admin-scripts
RUN mkdir -p /opt/admin-scripts-output && chown mumble:alex /opt/admin-scripts-output && chmod 750 /opt/admin-scripts-output

EXPOSE 20 22 2121
CMD ["/usr/bin/supervisord"]
