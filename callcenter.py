class Call(object):
	def __init__(self,u_id,name,phone_numb,call_time,call_reason):
		self.u_id = u_id
		self.name = name
		self.phone_numb = phone_numb
		self.call_time = call_time
		self.call_reason = call_reason
	def display(self):
		print self.u_id
		print self.name
		print self.phone_numb
		print self.call_time
		print self.call_reason


class Call_Center(object):
	def __init__(self):
		self.calls = []
		self.queue = self.countqueue()
	def add(self,callitem):
		self.calls.append(callitem)
		
	def remove(self,rcall):
		self.calls.remove(rcall)
		
	def countqueue(self):
		return len(self.calls)

	def removewithnumb(self,danumba):
		for i in self.calls:

	def info(self):
		for call in self.calls:
			call.display()

print "Call 1"
call1 = Call("id 1","Brian","000-000-0000","0:49","to say hello")

call1.display()

callcenter1 = Call_Center()
callcenter1.add(call1)
callcenter1.info()

ANSWER
-----
ANSWER

from datetime import datetime

class Call(object):
    NUM_CALLS = 0
    def __init__(self, caller, phone_num, reason):
        self.caller = caller
        self.phone_num = phone_num
        self.time_of_call = datetime.now()
        self.reason = reason
        self.id = Call.NUM_CALLS
        
        Call.NUM_CALLS += 1
    
    def display_info(self):
        print "\n" + ("#" * 20)
        for attr, val in self.__dict__.iteritems():
            if attr == "time_of_call":
                print "{}: {}".format(attr, val.strftime("%I:%M:%S"))
            else:
                print "{}: {}".format(attr, val)
        print "#" * 20

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue_size = self.get_queue_size()

    def get_queue_size(self):
        return len(self.calls)

    def add(self, a_call):
        self.calls.append(new_call)

    def remove(self, r_call):
        self.calls.remove(r_call)

    def info(self):
        for call in self.calls:
            call.display_info()


'''
You can run this file to interactively add calls
'''


def handle_call():
    print "Would You like to make a call?"
    print "type [1] for yes and [0] for no"
    ans = raw_input()
    return int(ans)

def take_call():
    print "What is your name?"
    name = raw_input()
    print "What is your reason for calling?"
    reason = raw_input()
    print "Please confirm your phone number"
    num = raw_input()
    print "Please stay on the line while we proccess your call"
    return Call(name, num, reason)

game_on = True
center = CallCenter()
while game_on:
    ring = handle_call()
    if ring == 1:
        center.calls.append(take_call())
        print "All calls today:"
        center.info()
    else:
        game_on = False
