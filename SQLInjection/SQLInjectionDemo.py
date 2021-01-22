# coding: utf-8

"""
    Demonstrate 
    - sql injection
    - and how to protect from it
    on PostgreSQL

    Reference : https://blog.netwrix.fr/2018/07/04/les-10-types-de-cyberattaques-les-plus-courants/
"""

import psycopg2

def Main():
    """
        Main entry
        Note : little_db must be created prior to run this
    """

    print("\nSQL INJECTION demo")
    print("------------------\n")

    # create connection
    MyConnection = psycopg2.connect("dbname=little_db user=postgres password=PG20")
    
    # no DB
    if MyConnection is None:
        print("little_db database must be created prior to run this demo.\n")
        return
    else:
        MyConnection.autocommit = True
        print("Connected to little_db database.\n")

    # define DB script creation
    SQLInstructions = """
        DROP TABLE IF EXISTS public.user_data;

        CREATE TABLE public.user_data (
            id serial NOT NULL,
            pseudo varchar(30) NOT NULL,
            user_id varchar(30) NOT NULL,
            user_password varchar(10) NOT NULL,
            CONSTRAINT user_data_pk PRIMARY KEY (id)
        );

        INSERT INTO public.user_data (pseudo, user_id, user_password) VALUES
            ('Alain', 'alain', 'a1'),
            ('Corinne', 'cori', 'c2'),
            ('Isabelle', 'isa', 'i3');
        """
    
    # execute script
    with MyConnection.cursor() as MyCursor:
        for Instruction in SQLInstructions.split(";"):
            Instruction = Instruction.strip()
            # print(Instruction)
            # check if instruction is empty
            if Instruction:
                # execute instruction
                MyCursor.execute(Instruction)
                # commit to DB
                MyConnection.commit()

    # demo loop
    QuitDemo = False
    while not QuitDemo:

        # check existing data
        print("\nActual data in user_data table :")
        MyQuery = "SELECT * FROM user_data ORDER BY user_data.pseudo"
        with MyConnection.cursor() as MyCursor:
            MyCursor.execute(MyQuery)
            Results = MyCursor.fetchall()
            if Results:
                for Result in Results:
                    print(Result)
            else:
                print("There is no data in user_data table !")

        # ask to connect
        UserChoice = input("\nTry connecting with (V)ulnerability or (S)afe or (Q)uit ? ")
        if UserChoice.lower() == "q":
            QuitDemo = True
        elif UserChoice.lower() == "v":
            print("Vulnerability mode choosen")
        else:
            print("Safe mode choosen")

        if not QuitDemo:
            print("\nExample of vulnerabilties to try :\n    → enter ';-- after a valid user ID\n    → enter ' or 1 --- as password\n    → enter after user ID or password : '; DELETE FROM user_data RETURNING id;--")
            
            # ask credentials
            UserID = input("\nEnter a user ID : ")
            UserPassword = input("Enter password : ")
            
            # define and execute query depending on choosen mode
            Results = None
            try:
                if UserChoice.lower() == "v":
                    MyQuery = "SELECT user_data.pseudo FROM user_data WHERE user_data.user_id = '" + UserID + "' AND user_data.user_password = '" + UserPassword + "';"
                    with MyConnection.cursor() as MyCursor:
                        MyCursor.execute(MyQuery)
                        Results = MyCursor.fetchall()
                else:
                    MyQuery = "SELECT user_data.pseudo FROM user_data WHERE user_data.user_id = %s AND user_data.user_password = %s"
                    with MyConnection.cursor() as MyCursor:
                        MyCursor.execute(MyQuery, (UserID, UserPassword))
                        Results = MyCursor.fetchall()
            except(Exception, psycopg2.DatabaseError) as Error:
                # error
                print(f"\nDBError : {Error}")
           
            # get results
            if Results is None:
                print(f"\nOops, it seems like a curious request...")
            elif len(Results) == 1:
                print(f"\nHello {Results[0][0]}, you are connected.")
            else:
                print(Results)
                print(f"\nSorry, wrong credentials.")

    # end of demo
    MyConnection.close()
    print("\nGoodbye, don't forget to drop little_db database if your are done with this demo.\n")


# program entry
if __name__ == "__main__":    
    Main()
