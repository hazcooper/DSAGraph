import copy
import math
from DSAHashEntry import DSAHashEntry
import numpy as np
import csv


#
# Author     : Daniel Millband
# ID         : 21024382
#
# DSAHashTable.py - class for hash table
#
# Revisions  : 5/10/2023 - created
#
#
class DSAHashTable:

    def __init__(self, table_size):

        self.actual_size = self._find_next_prime(table_size)
        self.hash_array = np.empty(self.actual_size, dtype=object)
        self.count = 0  # initialize the count of items in the table to 0
        self.resizing = False

        for number in range(self.actual_size):
            self.hash_array[number] = DSAHashEntry()

    def get_item(self, in_key):
        table_size = len(self.hash_array)
        hash_index = self._other_hash(in_key)
        original_index = hash_index
        found = False
        give_up = False

        # hash_index_object = self.hash_array[hash_index]

        while not found and not give_up:
            if self.hash_array[hash_index].get_state() == 0:
                give_up = True
            elif self.hash_array[hash_index].get_key() == in_key:
                found = True
            else:
                hash_index = self._step_hash(in_key)
                if hash_index == original_index:
                    give_up = True

        # exception handling
        if not found:
            raise ValueError("The key was not found")

        return self.hash_array[hash_index].get_value()

    def put_item(self, in_key, in_value):
        table_size = len(self.hash_array)
        hashed_key = self._other_hash(in_key)
        original_index = hashed_key

        while self.hash_array[hashed_key].get_state() != 0 and self.hash_array[hashed_key].get_key() != in_key:
            # calculating the hash step size using step size function
            hashed_key = (hashed_key + self._step_hash(in_key)) % table_size
            if hashed_key == original_index:
                raise Exception("Hash Table is full!")

        self.hash_array[hashed_key].set_key(in_key)
        self.hash_array[hashed_key].set_value(in_value)
        self.count += 1
        self.hash_array[hashed_key].set_state(1)
        print("Item inserted into the hash table")
        print("Current load factor : " + str(self.get_load_factor()))

        if not self.resizing:
            # getting load factor value to compare against
            load_factor = self.get_load_factor()
            # setting threshold
            upper_threshold = 0.60

            if load_factor >= upper_threshold:
                print(str(load_factor) + " is greater than " + str(upper_threshold))
                print("Resizing of the hash table will happen!")

                print("Setting count to 0")
                self.count = 0
            # calling resize function
                self._resize_upper(table_size)

                print("New size of hash table: " + str(len(self.hash_array)))

    def remove(self, in_key):
        table_size = len(self.hash_array)
        hashed_key = self._other_hash(in_key)
        original_index = hashed_key

        while self.hash_array[hashed_key].get_state() != 0 and self.hash_array[hashed_key].get_key() != in_key:
            hashed_key = self._step_hash(in_key)
            if hashed_key == original_index:
                raise Exception("Key not in hash table")

        self.hash_array[hashed_key].set_key("")
        self.hash_array[hashed_key].set_value(None)
        self.hash_array[hashed_key].set_state(-1)
        self.count -= 1

        print("Item removed from the hash table")
        print("Current load factor : " + str(self.get_load_factor()))

        if not self.resizing:
            load_factor = self.get_load_factor()
            lower_threshold = 0.25

            if load_factor < lower_threshold:
                print(str(load_factor) + " is lower than " + str(lower_threshold))
                print("Resizing of the hash table will happen!")

                self.count = 0
                self._resize_lower(table_size)

                print("New size of hash table: " + str(len(self.hash_array)))

    def get_load_factor(self):
        # settings threshold values for now
        table_size = len(self.hash_array)

        total_count = self.count

        load_factor = total_count / table_size

        return load_factor

    def export(self):

        # write to CSV
        with open('output_file', mode='w', newline='') as file:
            csv_writer = csv.writer(file, delimiter=',')

            for number in range(self.actual_size):
                if self.hash_array[number].get_state() != 0:
                    key = self.hash_array[number].get_key()
                    value = self.hash_array[number].get_value()
                    csv_writer.writerow([key, value])

    def _resize_upper(self, capacity):

        self.resizing = True
        print("\n----Resizing----")
        # copying values from hash array into old array variable
        # old_array = self.hash_array
        old_array = self.hash_array.copy()
        new_size = self._find_next_prime(capacity * 2)
        new_size = int(new_size)
        self.hash_array = np.empty(new_size, dtype=object)

        # initializing new hash array with hash entry objects in each slot
        for number in range(new_size):
            self.hash_array[number] = DSAHashEntry()

        for i in range(len(old_array)):
            if old_array[i].get_state() != 0:
                if old_array[i].get_value() is not None:
                    # print(old_array[i].get_key())
                    self.put_item(old_array[i].get_key(), old_array[i].get_value())

        self.resizing = False
        print("\n----Resizing finished----")

    def _resize_lower(self, capacity):

        self.resizing = True
        print("\n----Resizing----")

        old_array = self.hash_array.copy()
        new_size = self._find_next_prime(capacity / 2)
        new_size = int(new_size)
        self.hash_array = np.empty(new_size, dtype=object)

        for number in range(new_size):
            self.hash_array[number] = DSAHashEntry()

        for i in range(len(old_array)):
            if old_array[i].get_state() != 0:
                if old_array[i].get_value is not None:
                    self.put_item(old_array[i].get_key(), old_array[i].get_value())

        self.resizing = False
        print("\n----Resizing finished----")

    def print_table(self, hash_table):

        print("\nHash Table")
        print("-------------------")

        for i, entry in enumerate(self.hash_array):
            # Let's assume a state of 0 means empty and we only print occupied slots.
            # Adjust this check based on your actual state values for occupied and empty/deleted slots.
            if entry.get_state() != 0:
                print(f"Index:{i}, Key:{entry.get_key()}, Value:{entry.get_value()}")

        print("-------------------\n")

        # print("Hash Table")
        # print("-------------------")
        #
        # for i in range(len(hash_table)):
        #     if hash_table[i].get_state() == 1:
        #         print(f"Index:{i}", Key:{hash_table[i].get_key()}, Value:{hash_table[i].get_value()})
        #
        # print("-------------------\n")

    def _simple_hash(self, string):
        prime_number = 31
        sum_of_characters = 0
        for character in string:
            sum_of_characters += ord(character)

        return sum_of_characters % prime_number

    def _other_hash(self, key):
        hash_index = 0

        for character in key:
            hash_index = (31 * hash_index) + ord(character)

        return hash_index % len(self.hash_array)

    def _find_next_prime(self, start_value):
        if start_value % 2 == 0:
            prime_value = start_value - 1
        else:
            prime_value = start_value

        is_prime = False
        # test if prime_value is actually a prime number
        while not is_prime:
            prime_value = prime_value + 2
            ii = 3
            is_prime = True
            root_value = math.sqrt(prime_value)
            while ii <= root_value and is_prime:
                if prime_value % ii == 0:
                    is_prime = False
                else:
                    ii = ii + 2

        return prime_value

    def _step_hash(self, in_key):
        # constant
        MAX_STEP = 67
        sum_of_chars = 0
        for character in in_key:
            sum_of_chars += ord(character)

        hash_step = MAX_STEP - (sum_of_chars % MAX_STEP)  # Step size will be between 1 and MAX_STEP

        return hash_step

    def _find_key(self, in_key):
        table_size = len(self.hash_array)
        hashed_key = self._simple_hash(in_key)
        original_index = hashed_key

        while self.hash_array[hashed_key].get_state() != 0:
            if self.hash_array[hashed_key].get_key() == in_key:
                return self.hash_array[hashed_key].get_value()

            hashed_key = (hashed_key + 1) % table_size

            if hashed_key == original_index:
                raise Exception("Not in hash table")
