#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 13:29:32 2022

@author: tejareddy
"""

import csv
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str,
                        help="csv path")
    parser.add_argument("-d", help="date to search")
    args = parser.parse_args()
    if(args.d != None and args.path != None):
        most_active_cookie(args.path, args.d)

        


def most_active_cookie(path, target_date):
    # create a list of each time a cookie is active on target date
    day_list = []
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            # check if timestamp is on target day
            if line_count != 0:
                date = row[1][:10]
                # add cookie to target day list
                if date == target_date:
                    day_list.append(row[0])
                    
            line_count += 1
            
    # creates a list to hold the max occuring cookies
    most_active = []
    # a dict to hold the number of times the most active cookies havebeen seen
    times_seen = {}
    
    
    for cookie in day_list:
        if len(most_active) == 0:
            most_active.append(cookie)
            times_seen[cookie] = 1
        else:
            if cookie in times_seen:
                times_seen[cookie] += 1
            else:
                times_seen[cookie] = 1
            if cookie in most_active:
                most_active = [cookie]
            elif times_seen[cookie] == times_seen[most_active[0]]:
                most_active.append(cookie)
    
    for cookie in most_active:
        print(cookie)
    return most_active
    
if __name__ =="__main__":
    main()
    