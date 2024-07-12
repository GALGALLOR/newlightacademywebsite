from flask_mysqldb import MySQL
from flask import  get_flashed_messages, session,Flask,render_template,redirect,request,flash,url_for
app=Flask(__name__)

mydb=MySQL(app)


app.config['MYSQL_HOST']=''
app.config['MYSQL_USER']=''
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']=''

app.secret_key='mimi'
def most_frequent(List):
    counter = 0
    num = List[0]

    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i

    return num

@app.route('/',methods=['POST','GET'])
def home():
    if request.method == 'POST':
        session.permanent= True
        name=request.form['name']
        form=request.form['form']
        category=request.form['category']
        session['name']=name
        session['form']=form
        session['category']=category
        if category=='football':
            return redirect(url_for('footballquestions'))
        elif category=='basketball':
            return redirect(url_for('basketballquestions'))
        else:
            return redirect(url_for('volleyballquestions'))
    else:
        if 'name' in session:
            session.pop('name')
            if 'form' in session:
                session.pop('form')
                if 'category' in session:
                    session.pop('category')
                    flash('logged out successfully')
        return render_template('Home.html')



@app.route('/footballquestions',methods = ['POST','GET'])
def footballquestions():
    if request.method =='POST':

        st = request.form['st']
        lw=request.form['lw']
        rw=request.form['rw']
        mid10=request.form['mid10']
        mid8=request.form['mid8']
        cdm=request.form['cdm']
        cb4=request.form['cb4']
        cb5=request.form['cb5']
        lb=request.form['lb']
        rb=request.form['rb']
        gk=request.form['gk']

        session.permanent= True
        name=session['name']
        form=session['form']
        print(name,form,st,lw,rw,mid10,mid8,cdm,cb4,cb5,rb,lb,gk)


        cursor=mydb.connection.cursor()
        cursor.execute('SELECT * FROM USERDATA WHERE name="'+name+'" AND form="'+form+'"')
        l=cursor.fetchall()
        print(l)
        L='test'
        for L in l:
            pass
        details=L
        print('details is ',details)
        if details==None:
            cursor=mydb.connection.cursor()
            cursor.execute('INSERT INTO USERDATA(NAME,FORM,st,lw,rw,mid10,mid8,cdm,lb,rb,cb4,cb5,gk)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(name,form,st,lw,rw,mid10,mid8,cdm,lb,rb,cb4,cb5,gk))
            mydb.connection.commit()
            return redirect(url_for('leaderboardfootball'))
        if name==details[0] and form==details[1]:
            cursor.execute('UPDATE USERDATA SET st=%s,lw=%s,rw=%s,mid10=%s,mid8=%s,cdm=%s,cb5=%s,cb4=%s,rb=%s,lb=%s,gk=%s WHERE NAME=%s AND FORM=%s ',(st,lw,rw,mid10,mid8,cdm,cb5,cb4,rb,lb,gk,name,form))
            mydb.connection.commit()
            print('Printing the new details')
            return redirect(url_for('leaderboardfootball'))
        else:
            cursor=mydb.connection.cursor()
            cursor.execute('INSERT INTO USERDATA(NAME,FORM,st,lw,rw,mid10,mid8,cdm,lb,rb,cb4,cb5,gk)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(name,form,st,lw,rw,mid10,mid8,cdm,lb,rb,cb4,cb5,gk))
            mydb.connection.commit()
            return redirect(url_for('leaderboardfootball'))
    else:
        if 'name' in session:

            return render_template('footballQuestions.html')
        else:
            flash('You have to Enter Your name and Class first')
            return redirect(url_for('home'))

###
###
###
####separator for football and basketball
#####
#####
#######
#######
@app.route('/basketballquestions',methods = ['POST','GET'])
def basketballquestions():
    if request.method =='POST':

        c =str( request.form['centerplayer'] )
        pg=str( request.form['pointguard']   )
        sg=str( request.form['shootingguard']) 
        sf=str( request.form['smallfoward']  )
        pf=str( request.form['powerfoward']  )



        session.permanent= True
        name=session['name']
        form=session['form']
        print(name,form,c,pg,sg,sf,pf)


        cursor=mydb.connection.cursor()
        cursor.execute('SELECT * FROM BASKETBALL WHERE name="'+name+'" AND form="'+form+'"')
        l=cursor.fetchall()
        print(l)
        L='test'
        for L in l:
            pass
        details=L
        print('details is ',details)
        if details==None:
            cursor=mydb.connection.cursor()
            cursor.execute('INSERT INTO BASKETBALL(NAME,FORM,c,pg,sg,sf,pf)VALUES(%s,%s,%s,%s,%s,%s,%s)',(name,form,c,pg,sg,sf,pf))
            mydb.connection.commit()
            return redirect(url_for('leaderboardbasketball'))
        if name==details[0] and form==details[1]:
            cursor.execute('UPDATE BASKETBALL SET pg=%s, sg=%s, sf=%s, pf=%s, c=%s WHERE NAME=%s AND FORM=%s ',(pg,sg,sf,pf,c,name,form))
            mydb.connection.commit()
            print('Printing the new details')
            return redirect(url_for('leaderboardbasketball'))
        else:
            cursor=mydb.connection.cursor()
            cursor.execute('INSERT INTO BASKETBALL(name,form,c,pg,sg,sf,pf)VALUES(%s,%s,%s,%s,%s,%s,%s)',(name,form,c,pg,sg,sf,pf))
            mydb.connection.commit()
            return redirect(url_for('leaderboardbasketball'))
    else:
        if 'name' in session:

            return render_template('basketballQuestions.html')
        else:
            flash('You have to Enter Your name and Class first')
            return redirect(url_for('home'))

###vol
###                             volllllll
###
####separator for volleyball and the rest
#####
#####
#######
#######
@app.route('/volleyballquestions',methods = ['POST','GET'])
def volleyballquestions():
    if request.method =='POST':

        ca =str( request.form['centralattacker'] )
        la=str( request.form['leftattacker']   )
        ra=str( request.form['rightattacker']) 
        libero=str( request.form['libero']  )
        s=str( request.form['setter']  )



        session.permanent= True
        name=session['name']
        form=session['form']
        print(name,form,ca,la,ra,s,libero)


        cursor=mydb.connection.cursor()
        cursor.execute('SELECT * FROM VOLLEYBALL WHERE name="'+name+'" AND form="'+form+'"')
        l=cursor.fetchall()
        print(l)
        L='test'
        for L in l:
            pass
        details=L
        print('details is ',details)
        if details==None:
            cursor=mydb.connection.cursor()
            cursor.execute('INSERT INTO VOLLEYBALL(NAME,FORM,ca,la,ra,libero,s)VALUES(%s,%s,%s,%s,%s,%s,%s)',(name,form,ca,la,ra,libero,s))
            mydb.connection.commit()
            return redirect(url_for('leaderboardvolleyball'))
        if name==details[0] and form==details[1]:
            cursor.execute('UPDATE VOLLEYBALL SET la=%s, ca=%s, ra=%s, libero=%s, s=%s WHERE NAME=%s AND FORM=%s ',(la,ca,ra,libero,s,name,form))
            mydb.connection.commit()
            print('Printing the new details')
            return redirect(url_for('leaderboardvolleyball'))
        else:
            cursor=mydb.connection.cursor()
            cursor.execute('INSERT INTO VOLLEYBALL(NAME,FORM,ca,la,ra,libero,s)VALUES(%s,%s,%s,%s,%s,%s,%s)',(name,form,ca,la,ra,libero,s))
            mydb.connection.commit()
            return redirect(url_for('leaderboardvolleyball'))
    else:
        if 'name' in session:

            return render_template('volleyballquestions.html')
        else:
            flash('You have to Enter Your name and Class first')
            return redirect(url_for('home'))




@app.route('/home')
def base():
    return redirect(url_for('home'))

@app.route('/leaderboardfootball')
def leaderboardfootball():
    if 'name' in session:
        session.pop('name')
        if 'form' in session:
            session.pop('form')
            if 'category' in session:
                session.pop('category')
    cursor = mydb.connection.cursor()
    #start
    cursor.execute('SELECT st FROM USERDATA')
    mimi=cursor.fetchall()
    striker_sample=[]
    for people in mimi:
        striker_sample.append(people[0])
    st = most_frequent(striker_sample)
    #end
        #start
    cursor.execute('SELECT lw FROM USERDATA')
    mimi=cursor.fetchall()
    lw=[]
    for people in mimi:
        lw.append(people[0])
    lw = most_frequent(lw)
    #end
            #start
    cursor.execute('SELECT rw FROM USERDATA')
    mimi=cursor.fetchall()
    rw=[]
    for people in mimi:
        rw.append(people[0])
    rw = most_frequent(rw)
    #end
        #start
    cursor.execute('SELECT mid10 FROM USERDATA')
    mimi=cursor.fetchall()
    mid10=[]
    for people in mimi:
        mid10.append(people[0])
    mid10 = most_frequent(mid10)
    #end
            #start
    cursor.execute('SELECT mid8 FROM USERDATA')
    mimi=cursor.fetchall()
    mid8=[]
    for people in mimi:
        mid8.append(people[0])
    mid8 = most_frequent(mid8)
    #end
    #start
    cursor.execute('SELECT cdm FROM USERDATA')
    mimi=cursor.fetchall()
    cdm=[]
    for people in mimi:
        cdm.append(people[0])
    cdm = most_frequent(cdm)
    #end
        #start
    cursor.execute('SELECT lb FROM USERDATA')
    mimi=cursor.fetchall()
    lb=[]
    for people in mimi:
        lb.append(people[0])
    lb = most_frequent(lb)
    #end
            #start
    cursor.execute('SELECT rb FROM USERDATA')
    mimi=cursor.fetchall()
    rb=[]
    for people in mimi:
        rb.append(people[0])
    rb = most_frequent(rb)
    #end
        #start
    cursor.execute('SELECT cb4 FROM USERDATA')
    mimi=cursor.fetchall()
    cb4=[]
    for people in mimi:
        cb4.append(people[0])
    cb4 = most_frequent(cb4)
    #end
            #start
    cursor.execute('SELECT cb5 FROM USERDATA')
    mimi=cursor.fetchall()
    cb5=[]
    for people in mimi:
        cb5.append(people[0])
    cb5 = most_frequent(cb5)
    #end
        #start
    cursor.execute('SELECT gk FROM USERDATA')
    mimi=cursor.fetchall()
    gk=[]
    for people in mimi:
        gk.append(people[0])
    gk = most_frequent(gk)
    #end

    #print(STRIKER,WINGER,MIDFIELDER,FULLBACK,CENTER_BACK,GOALIE,MANAGER)#

    return render_template('leaderboardfootball.html',st=st,lw=lw,rw=rw,mid10=mid10,mid8=mid8,cdm=cdm,rb=rb,lb=lb,cb4=cb4,cb5=cb5,gk=gk)



@app.route('/leaderboardbasketball')
def leaderboardbasketball():
    if 'name' in session:
        session.pop('name')
        if 'form' in session:
            session.pop('form')
            if 'category' in session:
                session.pop('category')
    cursor = mydb.connection.cursor()
    #start
    cursor.execute('SELECT pg FROM BASKETBALL')
    mimi=cursor.fetchall()
    striker_sample=[]
    for people in mimi:
        striker_sample.append(people[0])
    pg = most_frequent(striker_sample)
    #end
        #start
    cursor.execute('SELECT sg FROM BASKETBALL')
    mimi=cursor.fetchall()
    lw=[]
    for people in mimi:
        lw.append(people[0])
    sg = most_frequent(lw)
    #end
            #start
    cursor.execute('SELECT sf FROM BASKETBALL')
    mimi=cursor.fetchall()
    rw=[]
    for people in mimi:
        rw.append(people[0])
    sf = most_frequent(rw)
    #end
        #start
    cursor.execute('SELECT pf FROM BASKETBALL')
    mimi=cursor.fetchall()
    mid10=[]
    for people in mimi:
        mid10.append(people[0])
    pf = most_frequent(mid10)
    #end
            #start
    cursor.execute('SELECT c FROM BASKETBALL')
    mimi=cursor.fetchall()
    mid8=[]
    for people in mimi:
        mid8.append(people[0])
    c = most_frequent(mid8)
    #end
    
    #print(STRIKER,WINGER,MIDFIELDER,FULLBACK,CENTER_BACK,GOALIE,MANAGER)#

    return render_template('leaderboardbasketball.html',c=c,pg=pg,sg=sg,sf=sf,pf=pf)

@app.route('/leaderboardvolleyball')
def leaderboardvolleyball():
    if 'name' in session:
        session.pop('name')
        if 'form' in session:
            session.pop('form')
            if 'category' in session:
                session.pop('category')
    cursor = mydb.connection.cursor()
    #start
    cursor.execute('SELECT ca FROM VOLLEYBALL')
    mimi=cursor.fetchall()
    striker_sample=[]
    for people in mimi:
        striker_sample.append(people[0])
    ca = most_frequent(striker_sample)
    #end
        #start
    cursor.execute('SELECT la FROM VOLLEYBALL')
    mimi=cursor.fetchall()
    lw=[]
    for people in mimi:
        lw.append(people[0])
    la = most_frequent(lw)
    #end
            #start
    cursor.execute('SELECT ra FROM VOLLEYBALL')
    mimi=cursor.fetchall()
    rw=[]
    for people in mimi:
        rw.append(people[0])
    ra = most_frequent(rw)
    #end
        #start
    cursor.execute('SELECT libero FROM VOLLEYBALL')
    mimi=cursor.fetchall()
    mid10=[]
    for people in mimi:
        mid10.append(people[0])
    libero = most_frequent(mid10)
    #end
            #start
    cursor.execute('SELECT s FROM VOLLEYBALL')
    mimi=cursor.fetchall()
    mid8=[]
    for people in mimi:
        mid8.append(people[0])
    s = most_frequent(mid8)
    #end
    
    #print(STRIKER,WINGER,MIDFIELDER,FULLBACK,CENTER_BACK,GOALIE,MANAGER)#

    return render_template('leaderboardvolleyball.html',s=s,la=la,ra=ra,ca=ca,libero=libero)

@app.route('/score')
def score():
    return redirect(url_for('leaderboardfootball'))

@app.route('/scores')
def scores():
    return redirect(url_for('scores'))


@app.route('/logout')
def logout():
    session.pop('name')
    session.pop('form')
    session.pop('category')
    flash('logged out successfully')
    return redirect(url_for('home'))

if __name__ == '__main__':
    debug=True
    app.run()
