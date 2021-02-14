import os
import logging
import jaydebeapi


def set_environment(JAR_file_path: str, JDK_TAR_path: str):
    """
    Process to setup the environment
    1. Copy sqljdbc41.jar file and Copy jdk-8u181-linux-x64.tar.gz directory from staging bucket to the worker node /tmp directory.
    2. Create the environment directory /usr/lib/jvm on the worker node.
    3. Extract the files from tar present in /tmp directory to the environment directory /usr/lib/jvm.
    4. Create a symbolic link between the /usr/lib/jvm/jdk1.8.0_181/bin/java and /usr/bin/java so that the file extracted by us 
        can be accessed correctly while creating the connection.
        Symbolic links help us configuring environment variables without actually changing them.
    """

    # -- Copy sqljdbc41.jar to the worker node
    os.system(f'gsutil cp {JAR_file_path}/sqljdbc41.jar /tmp/')

    # -- Copy jdk-8u181-linux-x64.tar.gz directory to the worker node
    os.system(f'gsutil cp -r {JDK_TAR_path}/jdk-8u181-linux-x64.tar.gz /tmp/')
    # -r flag is required when we copy the directory

    logging.info('Jar and Java Libraries copied to Instance...')

    # Create the libraries directory
    os.system('mkdir -p /usr/lib/jvm')
    # -p flag makes sure that the directories in the path also gets created if they are not there.

    # unzip the tar file and copy to created directory above
    os.system('tar zxvf /tmp/jdk-8u181-linux-x64.tar.gz -C /usr/lib/jvm')
    """"
    z means (un)z̲ip.
    x means ex̲tract files from the archive.
    v means print the filenames v̲erbosely.
    f means the following argument is a f̱ilename.
    """ 

    # create a symbolic link to the java environment variable to the extracted java file from tar.
    os.system('update-alternatives --install "/usr/bin/java" "java" "/usr/lib/jvm/jdk1.8.0_181/bin/java" 1')

    # configure the variable to use
    os.system('update-alternatives --config java')

    logging.info('Environment Set.')


def read(host: str, port: int, database: str, user: str, password: str, query: str):
    jclassname = "com.microsoft.sqlserver.jdbc.SQLServerDriver"
    url = f'jdbc:sqlserver://{host}:{port};database={database};user={user};password={password}'
    jars = ["/tmp/sqljdbc41.jar"]
    libs = None
    cnx = jaydebeapi.connect(jclassname, url, jars=jars, libs=libs)
    logging.info("Connection Successful...")
    cursor = cnx.cursor()
    logging.info('Query is %s', query)
    logging.info('Query submitted to SqlServer Database')
    cursor.execute(query)
    cursor.close()
    cnx.close()
