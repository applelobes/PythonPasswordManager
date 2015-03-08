from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk

class App( Frame ):
    def __init__( self, master = None ):
        ttk.Frame.__init__( self, master )
        self.master.title( "Password Manager" )
        self.master = master
        self.init_window()
        self.menu_Bar()

    def init_window( self ):
        #self.style = ttk.Style()
        #self.style.theme_use( "default" )
        panel1 = Frame( self )
        panel1.config()
        panel1.pack( fill = X, padx = 25 )
        
        label1 = ttk.Label( panel1, text = 'Password Manager' )
        label1.config( background = "cornflower blue", anchor = CENTER, font = ( "times", 32) )
        label1.pack( fill = X, pady = 10 )
        label2 = ttk.Label( panel1, text = """The Password Manager will help solve all of your password needs.
                Enter a password for validation rules checkng, strength checking, of simoly generate a
                random password. Additionally, the application will give you the option to try and crack
                a password using several different techniques""" )
        label2.config( background = "light grey", font = ( "times", 16) )
        label2. pack( fill = X, pady = 10 )
        label3 = ttk.Label( panel1, text = 'Password Tasks:' )
        label3.config( background = "dark slate gray", foreground = "white", anchor = W, font = ( "times", 16))
        label3.pack( fill = X, pady = 10 )
        label4 = ttk.Label( panel1, text = 'Selelct an Option Below to get Started' )
        label4.config( background = "dark slate gray", foreground = "white" )
        label4.pack()
        label5 = ttk.Label( panel1, text = "Check password for validation rules" )
        label5.config( font = ( "times", 16) )
        label5.pack( fill = X, pady = 10 )
        label6 = ttk.Label( panel1, text = "Create a Random Password to Use" )
        label6.config( font = ( "times", 16) )
        label6.pack( fill = X, pady = 10 )
        label7 = ttk.Label( panel1, text = "Check the Strength of your Password" )
        label7.config( font = ( "times", 16) )
        label7.pack( fill = X, pady = 10 )
        label8 = ttk.Label( panel1, text = "Try and Crack a Password" )
        label8.config( font = ( "times", 16) )
        label8.pack( fill = X, pady = 10 )
        label9 = ttk.Label( panel1, text = "Encrypt a Password" )
        label9.config( font = ( "times", 16) )
        label9.pack( fill = X, pady = 10 )

        self.pack( fill = BOTH, expand = 1 )
        exitButton = ttk.Button( panel1, text = "Exit", command = self.exit_Button )
        #exitButton.place( x = 0, y = 0 )
        exitButton.pack( side = LEFT )

        self.pack( fill = BOTH, expand = 1 )
        demoButton = ttk.Button( panel1, text = "Contact Us", command = self.demo_Button )
        #demoButton.place( x = 0, y = 0 )
        demoButton.pack( side = LEFT )

        self.pack( fill = BOTH, expand = 1 )
        contactButton = ttk.Button( panel1, text = "Contact Us", command = self.contact_Button )
        #contactButton.place( x = 0, y = 0 )
        contactButton.pack( side = LEFT )
    
    def menu_Bar( self ):
        # create a menu for the menubar and associate it
        # with the window
        menu = Menu( self.master, tearoff = False )
        self.master.config( menu = menu )

        # create a File menu and add it to the menubar
        file = Menu( menu )
        file.add_command( label = "Exit")
        menu.add_cascade( label = "File", menu = file )
        helps = Menu ( menu )
        menu.add_cascade( label = "Help", menu = helps )

    def exit_Button( self ):
        self.quit()

    def demo_Button( self ):
        print( "Under Construction" )
        
    def contact_Button( self ):
        print( "Contact Us" )
        
def main():
    root = Tk()
    root.geometry( "950x750+350+50" )
##        background_image = Image.open( "GridW.gif" )
##        tkimage = ImageTk.PhotoImage( background_image )
##        Label( self.master, compound = CENTER, image = tkimage ).pack()    
    app = App( root )
    root.mainloop()

if __name__=='__main__':
    main()
