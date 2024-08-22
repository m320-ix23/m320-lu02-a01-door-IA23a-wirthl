class Door:
    """
    Diese Klasse beschreibt eine Türe mit der Eigenschaft
    door_is_open (für geöffnete Türe) sowie door_is_locke
    Die Türe überwacht die beiden Zustände und verhindert
    Das verriegeln selber delegiert die Türe an ein Objek
    """

    # Mit dem Keyword def wird eine Funktion bzw. eben
    # Der Konstruktor trägt IMMER den Namen __init__ und
    # Danach folgen die Übergabeparameter, deren Werte d
    # Attribute können aber auch mit einem fixen Wer
    # Konstruktoren werden als Erstes im Programm ang
    def __init__(self, ref2door_lock, base_color):
        """
        Erzeugt ein Tür-Objekt.
        :param ref2door_lock:
        :param base_color:
        """
        # ein privates Attribut muss im Konstruktor initi
        # über self._name_des_Attributs ansprechbar.
        self._the_door_lock = ref2door_lock
        # Hier wird der Setter eines Attributs aufgeruf
        self.color = base_color
        self._door_is_open = False
        self._door_is_locked = False

    # Nach den Konstruktoren folgen Methoden, die eine
    # Danach folgen Methoden, die auf ein Ereignis reagi
    def open_the_door(self):
        """
        Methode für das öffnen der Türe.
        Das ist aber nur möglich, wenn die Türe nicht
        """
        if self._door_is_locked == False:
            self._door_is_open = True

    def close_the_door(self):
        """
        Methode für das schliessen der Türe.
        Das geht immer, auch wenn die Türe schon geschlosse
        """
        self._door_is_open = False

    def lock_the_door(self):
        """
        Methode für das verriegeln der Türe.
        Das ist nur möglich, wenn die Türe nicht offen is
        Für das verriegeln ist aber das Türschloss zustän
        """
        if self._door_is_open == False:
            self._door_is_locked = self._the_door_lock.lock()

    def unlock_the_door(self):
        """
        Methode für das entriegeln der Türe
        Das ist nur möglich, wenn die Türe verriegelt ist.
        Für das entriegeln ist aber das Türschloss zuständ
        """
        if self._door_is_locked:
            self._door_is_locked = self._the_door_lock.unlock()

    def test(self):
        """
        schreibt alle Attribute in den StdOut
        """
        print(f'Türfarbe {self.color}'
              f'Türe offen: {self._door_is_open}'
              f'Türe verriegelt: {self._door_is_locked}')

    # Am Ende folgen die getter- und setter-Methoden für d
    # getter werden mit der Anotation @property markiert.
    @property
    def door_is_open(self):
        """
        getter-Methode für den Zustand door_is_open
        :return: true, wenn die Türe offen ist, sonst false
        """
        return self._door_is_open

    @property
    def door_is_locked(self):
        """
        getter-Methode für den Zustand door_is_locked
        :return: true, wenn die Türe verriegelt ist, sonst
        """
        return self._door_is_locked

    @property
    def color(self):
        """
        getter-Methode für die Eigenschaft color
        :return: die Farbe des Objekts
        """
        return self._color

    # setter werden mit der Anotation @name.setter
    @color.setter
    def color(self, new_color):
        """
        setter-Methode für die Eigenschaft color
        :param new_color:
        """
        self._color = new_color


"""
nur für die korrekte Übersetzung und Ausführung 
"""


class DoorLock:
    """
    dummy Klasse, damit in der Klasse Tuere kei
    """

    def __init__(self):
        print("ein Schloss erzeugt")

    def lock(self):
        return True

    def unlock(self):
        return False


# Hier die main-Methode festlegen
if __name__ == "__main__":
    print("Test für Tür-Objekt")
    the_door_lock = DoorLock()
    the_door = Door(the_door_lock, "grün")
    the_door.test()
    print("-- Türe jetzt öffnen")
    the_door.open_the_door()
    the_door.test()