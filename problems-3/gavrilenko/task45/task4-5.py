import collections
import itertools


class AlmostVector:
    """
    Mathematical vector with a basic vector operations
    """
    
    def __init__(self, *args):
        """
        creates a vector with specified coordinates

        :param *args: iterable object,

        """
        
        if len(args) == 1:
            if isinstance(args[0], collections.Iterable):
                self.__handle_iterable_obj(args[0])
            elif isinstance(args[0], (int, float, complex)):
                self._length = 1
                self._coordinates = (args[0],)
            else:
                raise TypeError
        elif len(args) > 1:
            self.__handle_iterable_obj(args)
        else:
            raise TypeError
    
    def __handle_iterable_obj(self, iterable):
        type_int = final_type = int
        type_float = float
        type_complex = complex
        self._length = 0
        it1, it2 = itertools.tee(iterable, 2)
        
        for element in it1:
            self._length += 1
            curr_el_type = type(element)
            if curr_el_type == type_float:
                if final_type == type_int:
                    final_type = type_float
            elif curr_el_type == type_complex:
                final_type = type_complex
            elif curr_el_type != type_int:
              raise TypeError("Wrong type found")
        
        self._coordinates = tuple((final_type(i) for i in it2))
        
    def __getitem__(self, item):
        """
        returns vector's 'item' coordinate

        :param item: number of coordinate to return
        :return: value of vector's 'item' coordinate

        """
        return self._coordinates[item]

    def __add__(self, other):
        """
        adds two vectors

        :param other: vector to add with
        :return: the result of adding two vectors

        """

        return AlmostVector(tuple(self[i] + other[i] for i in range(self._length)))

    def __sub__(self, other):
        """
        subtracts a vector from another vector

        :param other: vector for subtraction
        :return: the result of subtracting one vector from another

        """
        return AlmostVector(tuple(self[i] - other[i] for i in range(self._length)))

    def __mul__(self, other):
        """
        if 'other' is a scalar then
            multiplies the vector by this scalar
        if 'other' is a vector then
            returns dot product of two vectors

        :param other: scalar or another vector
        :return: dot product of two vectors or result of multiplying one vector by scalar
        :raise: TypeError exception if 'other' is not a number or vector

        """
        if isinstance(other, (int, float, complex)):
            return AlmostVector(tuple(self[i] * other for i in range(self._length)))
        elif isinstance(other, AlmostVector):
            return sum(self[i] * other[i] for i in range(self._length))
        else:
            raise TypeError("Wrong type: {}".format(type(other)))

    def __rmul__(self, other):
        """
        reverse multiplication (check __mul__ description)

        :param other: scalar or vector
        :return: dot product of two vectors or result of multiplying one vector by scalar

        """

        return self * other

    def __len__(self):
        """
        gets length of this vector

        :return: vector's length

        """

        return self._length

    def __str__(self):
        """
        gets string representation of this vector

        :return: this vector as a string

        """

        return str(self._coordinates)

    def __eq__(self, other):
        """
        compares two vectors

        :param other: vector to compare with
        :return: true if vectors are equal and false if not

        """

        return all(self[i] == other[i] for i in range(self._length))




