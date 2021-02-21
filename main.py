import play
from random import randint

play.set_backdrop((185, 119, 233))

status = 5
start_kub = play.new_box(color='red',height=40,width=100)
start_knopka = play.new_text('Start')
@play.repeat_forever
def restart999():
     global status
     if status == 5:
         status = 3
         podzkazka_dlia_ne_ochen_umnih = play.new_text('Извольте нажать SPACE !',color='red',y=-250)
         podzkazka_dlia_ne_ochen_umnih.hide()


        

         # bird_kub = play.new_box(color='black',transparency=0,width=32,height=25) 
         # bird = play.new_image(image = 'bird_1.png',size=140,x=0)
         # bird_kub.start_physics(can_move=True,obeys_gravity=True,stable=True,y_speed = 0)

         restart_kub = play.new_box(color='red',height=40,width=130,y=-70)
         restart_knopka = play.new_text('Restart',y = -70)
         restart_knopka.hide()
         restart_kub.hide()
         

       
 
@start_kub.when_clicked
def nazhatie():
    global status
    status = 4
    start_knopka.hide()
    start_kub.hide()
    podzkazka_dlia_ne_ochen_umnih.show()

def trubi_img(y_niz,rast):
    delta =515
    #truba_niz = play.new_image(image = 'truba_niz.png',size=210,y=y_niz,x=200)
    truba_niz = play.new_box(color = 'black',y=y_niz,x=500,transparency=50,width=45,height=500)
    truba_niz.status=1
    #truba_verh = play.new_image(image = 'truba_verh.png',size=290,y=delta + y_niz + rast,x=200)
    truba_verh = play.new_box(color = 'black',y=delta + y_niz + rast,x=500,transparency=50,width=45,height=530)
    return truba_niz,truba_verh



@play.repeat_forever
def start_program():
    global status
    if status == 4:
         if play.key_is_pressed('space'):
             podzkazka_dlia_ne_ochen_umnih.hide()

             status = 2
            
             bird_kub = play.new_box(color='black',transparency=0,width=32,height=25) 
             bird = play.new_image(image = 'bird_1.png',size=140,x=0)

             bird_kub.start_physics(can_move=True,obeys_gravity=True,stable=True,y_speed = 0)    

             bird_kub.y += 10
    if status ==2:




        global n
        n = 0

        status = 1

        chet = play.new_text(str(n),y=-30)
        chet.hide()



        # trubi_img(-200,100)

        trubi_list = []

        lose = play.new_text('YOU LOSE',color = 'red')
        lose.hide()


        @play.repeat_forever
        def keypads():
            if play.key_is_pressed('space'):
                bird_kub.y += 10
            

            

        @play.repeat_forever
        async def do():
            global status
            if status==1:
                a = trubi_img(randint(-500,-200),150)
                trubi_list.append(a)
                await play.timer(3)
            elif status==0:
                for tum in trubi_list:
                    tum[1].hide()
                    tum[0].hide()


        @play.repeat_forever  
        async def run():
            for i in trubi_list:
                i[0].x-=5
                i[1].x-=5
                if i[0].x < -500:
                    i[0].remove()
                    i[1].remove()
                    trubi_list.remove(i)



            
            await play.timer(1/40)



        @play.repeat_forever
        def touch():
            global status
            if status == 1:
                if bird_kub.y < -280:
                    bird_kub.stop_physics()
                    bird_kub.hide()
                    bird.remove()
                    lose.show()
                    chet.show()
                    restart_knopka.show()
                    restart_kub.show()
                    status = 0 
                elif status==1:
                    for truba in trubi_list:
                        if truba[0].is_touching(bird_kub) or truba[1].is_touching(bird_kub):
                            bird_kub.stop_physics()
                            bird_kub.hide()
                            bird.remove()
                            lose.show()
                            chet.show()
                            restart_knopka.show()
                            restart_kub.show()    
                            status = 0
                    



            bird.y = bird_kub.y

        @play.repeat_forever
        def chets():
            global n
            global status
            if status == 1:
                for tr in trubi_list:
                    if bird_kub.x > tr[1].x and tr[0].status==1:
                        tr[0].status= 0
                        n = n+1
                    
                        chet.words = str(n)     

        @restart_kub.when_clicked
        def restart():
            global status
            restart_kub.hide()
            restart_knopka.hide()
            status = 5
            start_knopka.show()
            start_kub.show()
            

            





play.start_program()
