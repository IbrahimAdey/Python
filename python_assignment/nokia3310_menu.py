menu = True
while menu:
	message = """

	Phone Menu:

	1: Phone book
	2: Message
	3: Chat
	4: Call register
	5: Tone
	6: Settings
	7: Call divert
	8: Games
	9: Calculator
	10: Remainders
	11: Clock
	12: Profiles
	13: SIM service
	

	"""
	print(message)

	select = int(input())

	match select:
		case 1:
			phonebookMenu = True
			while phonebookMenu:
				print("Phone book")
		
				message = """
				options:

				1: Search
				2: Service Nos
				3: Add name
				4: Erase
				5: Edit  
				6: Assign tone
				7: Send b'card
				8: Options
				9: Speed dials
				10: Voice tags
				0: Exit
				"""
				print(message)
	
				select = int(input())
				match select:
					case 1:
						search = True
						while search:
							print("Search")
							message = """
	
							0: Back
	
							"""
							print(message)
							selectPhonebook = int(input())
	
							match(selectPhonebook):
								case 0: search = False

								case _ : print("Invalid")

					case 2:
						serviceNos = True
						while(serviceNos):
							print("ServiceNos")
							message = """
	
							0: Back

							"""
							print(message)
							selectPhonebook = int(input())
	
							match(selectPhonebook):
								case 0: serviceNos = False
	
								case _: print("Invalid")


					case 3:
						Addname = True
						while(Addname):
							print("Add name");
							message = """
	
							0: Back
	
							"""
							print(message);
							selectPhonebook = int(input())
							match(selectPhonebook):
								case 0: Addname = false
		
								case _: print("Invalid")

					case 4:
						Erase = true
						while(Erase):
							print("Erase");
							message = """
	
							0: Back
				
							"""
							print(message)
							selectPhonebook = int(input())
							match(selectPhonebook):
								case 0: Erase = False
								case _: print("Invalid")


					case 5:
						Edit = True
						while(Edit):
							print("Edit")
							message = """

							0: Back

							"""
							print(message)
							selectPhonebook = int(input())
	
							match(selectPhonebook):
								case 0: Edit = False
								case _: print("Invalid")

					case 6:
						AssignTone = True
						while(AssignTone):
							print("Assign Tone")
							message = """
							0: Back
							"""
							print(message)
							selectPhonebook = int(input())
							match(selectPhonebook):
								case 0: AssignTone = False
								case _: print("Invalid")


					case 7:
						Sendbcard = True
						while(Sendbcard): 
							print("Send b' card")
							message = """
							0: Back
							"""
							print(message)
							selectPhonebook = int(input())
							match(selectPhonebook):
								case 0: Sendbcard = False
								case _: print("Invalid")


					case 8:
						Options = True
						while(Options): 
							print("Options")
							message = """
							
							1: Type of view
							2: Memory status
							0: Back 
							"""
							print(message);
							select = int(input())
							match(select):
								case 1:
									Typeofview = True
									while(Typeofview): 
										print("Types of view")
										message = """
										0: Back
										"""
										print(message)
										selectPhonebook = int(input())
										match(selectPhonebook):
											case 0: Typeofview = False
											case _: System.out.println("Invalid");


								case 2:
									MemoryStatus = True
									while(MemoryStatus): 
										print("Memory Status")
										message = """
										0: Back
										"""
										print(message)
										selectPhonebook = int(input())           
										match(selectPhonebook):
											case 0: MemoryStatus = False
											case _: print("Invalid")


								case 0: Options = False
								case _: print("Invalid")



					case 9:
						Speeddials = True
						while(Speeddials): 
							print("Speed dials")
							message = """
							0: Back
							"""
							print(message)
							selectPhonebook = int(input())
							match(selectPhonebook):
								case 0: Speeddials = False
								case _: print("Invalid");


					case 10:
						VoiceTags = True
						while(VoiceTags): 
							print("Voice Tags")
							message = """
							0: Back
							"""
							print(message)
							selectPhonebook = int(input())
							match(selectPhonebook):
								case 0: VoiceTags = False
								case _: print("Invalid")


					case 0:
						phonebookMenu = False
					case _: print("Error comand");




		case 2:
			Messages = True
			while(Messages): 
				print("Messages")
	
				message = """
	
				1: Write message
				2: Inbox
				3: Outbox
				4: Picture message
				5: Templates
				6: Smileys
				7: Message settings
				8: Info service
				9: Voice mailbox number
				10: Service command editor
				0: Back
	
				"""
				print(message)
				select = int(input())
				match(select):
	
					case 1:
						Writemessage = True
						while(Writemessage): 
							print("Writemessage")
							message = """
							0: Back
							"""
							print(message)
							selectPhonebook = int(input())
	
							match(selectPhonebook):
								case 0: Writemessage = False
	
								case _: print("Invalid")
	
	
	
					case 2:
						Inbox = True
						while(Inbox): 
							print("Inbox")
							message = """
							0: Back
							""";
							print(message);
							selectPhonebook = int(input())
	
							match(selectPhonebook):
								case 0: Inbox = False
	
								case _: print("Invalid")
	
	
	
					case 3:
						Outbox = True
						while(Outbox): 
							print("Outbox")
							message = """
							0: Back
							"""
							print(message)
							selectPhonebook = int(input())
	
							match(selectPhonebook):
								case 0: Outbox = False
								case _: print("Invalid")
	
	
					case 4:
						PictureMessage = True
						while(PictureMessage): 
							print("Picture Message")
							message = """
							0: Back
							"""
							print(message);
							selectPhonebook = int(input())
	
							match(selectPhonebook):
								case 0: PictureMessage = False
								case _: print("Invalid")
	
	
					case 5:
						Templates = True;
						while(Templates): 
							print("Templates")
							message = """
							0: Back
							"""
							print(message)
							selectPhonebook = int(input())
	
							match(selectPhonebook):
								case 0: Templates = False
								case _: print("Invalid")
	
					case 6:
						Smileys = True;
						while(Smileys): 
							print("Smileys")
							message = """	
							0: Back
							"""
							print(message);
							selectPhonebook = int(input())
	
							match(selectPhonebook):
								case 0: Smileys = False
								case _: print("Invalid")	
	
					case 7:
						MessageSetting = True
						while(MessageSetting): 
							print("Message settings")
	
							message = """	
							1: Set 1
							2: Common
							0: Back
	
							"""
							print(message)
							select = int(input())
	
							match(select):
								case 1:
									Set1 = True
									while(Set1): 
										print("Welcome to Set 1")
	
										message = """	
										1: Message centre number
										2: Message sent as
										3: Message validity
										0: Back
	
										"""
										print(message)
										select = int(input())
	
										match(select):
	
											case 1:
												MessageCentre = True
												while(MessageCentre): 
													print("Message Centre")
													message = """	
													0: Back
													"""
													print(message)
													selectPhonebook = int(input())
	
													match(selectPhonebook):
														case 0: MessageCentre = False
														case _: print("Invalid")
	
	
	
	
											case 2:
												SentAs = True
												while(SentAs): 
													print("Sent As")
													message = """	
													0: Back
	
													"""
													print(message)
													selectPhonebook = int(input())
	
													match(selectPhonebook):
														case 0: SentAs = False	
														case _: print("Invalid")
	
	
	
											case 3:
												MessageValidity = True
												while(MessageValidity): 
													print("Message Validity")
													message = """
													0: Back
													"""
													print(message)
													selectPhonebook = int(input())
	
													match(selectPhonebook):
														case 0: MessageValidity = False	
														case _: print("Invalid")
	
	
											case 0: Set1 = False
											case _: print("Invalid")
	
	
								case 2:
									Common = True
									while(Common): 
										print("Common")
	
										message = """	
										1: Delivery report
										2: Reply via same centre
										3: Character support
										0: Back
	
										"""
										print(message)
										select = int(input())
	
										match(select):
	
											case 1:
												DeliveryReport = True
												while(DeliveryReport): 
													print("Delivery Report")
													message = """	
													0: Back
													"""
													print(message);
													selectPhonebook = int(input())
	
													match(selectPhonebook):
														case 0: DeliveryReport = False
	
														case _: print("Invalid")
	
	
											case 2:
												ReplyViaCentre = True
												while(ReplyViaCentre): 
													print("Reply Via Centre")
													message = """	
													0: Back
													"""
													print(message)
													selectPhonebook = int(input())
	
													match(selectPhonebook):
														case 0: ReplyViaCentre = False
	
	
														case _: print("Invalid")
	
	
	
											case 3:
												CharacterSupport = True
												while(CharacterSupport): 
													print("Character Support")
													message = """	
													0: Back
													"""
													print(message)
													selectPhonebook = int(input())
	
													match(selectPhonebook):
														case 0: CharacterSupport = False
	
	
														case _: print("Invalid")
	
	
	
											case 0:
												Common = False
	
											case _: print("Invalid")
	
								case 0: MessageSetting = False
	
								case _: print("Invalid")
	
	
					case 8:
						InfoService = True
						while(InfoService): 
							print("Info Service")
							message = """	
							0: Back
							"""
							print(message)
							selectPhonebook = int(input())
	
							match(selectPhonebook):
								case 0: InfoService = False
	
								case _: print("Invalid")
	
	
	
					case 9:
						VoiceMailBoxMessage = True
						while(VoiceMailBoxMessage): 
							print("Voice Mail Box Message")
							message = """	
							0: Back
							"""
							print(message)
							selectPhonebook = int(input())
							match(selectPhonebook):
								case 0: VoiceMailBoxMessage = False
	
								case _: print("Invalid")
	
	
	
					case 10:
						Servicecommandeditor = True
						while(Servicecommandeditor): 
							print("Service command editor")
							message = """	
							0: Back
							"""
							print(message)
							selectPhonebook = int(input())
	
							match(selectPhonebook):
								case 0: Servicecommandeditor = False
								case _: print("Invalid")
	
	
					case 0:
						Messages = False
					case _: print("Error command");				
		
	
		case 3:
			Chat = True
			while(Chat): 
				print("Welcome to Chat");
				message = """
				0: Back
				"""
				print(message)
				selectPhonebook = int(input())

				match(selectPhonebook):
					case 0: Chat = False


					case _: print("Invalid");





		case 4:
			Callregister = True
			while(Callregister): 
				print("Call register");
				
				message = """
				
				1: Missed calls
				2: Recieving calls
				3: Dialled numbers
				4: Erase recent call lists
				5: Show call duration
				6: Show call costs
				7: call cost settings
				8: Prepaid credit
				0: Back
				"""
				print(message)
				select = int(input())
				
				match(select):
				
					case 1:
						MissedCall = True
						while(MissedCall): 
							print("Missed Call")
							message = """				
							0: Back
							"""
							print(message)
							selectPhonebook = int(input())
				
							match(selectPhonebook):
								case 0: MissedCall = False
								case _: print("Invalid")
				
				
					case 2:
						ReceivingCall = True
						while(ReceivingCall):  
							print("Receiving Call")
							message = """				
							0: Back
							"""
							print(message);
							selectPhonebook = int(input())
				
							match(selectPhonebook):
								case 0: ReceivingCall = False
								case _: print("Invalid");
				
				
					case 3:
						DialledNumber = True
						while(DialledNumber):  
							print("Dialled Number")
							message = """				
							0: Back
							"""
							print(message)
							selectPhonebook = int(input())
				
							match(selectPhonebook):
								case 0: DialledNumber = False
								case _: print("Invalid")
				
				
					case 4:
						EraseRecentCallList = True
						while(EraseRecentCallList):    
							print("Erase Recent Call List")
							message = """				
							0: Back
							"""
							print(message)
							selectPhonebook = int(input())
				
							match(selectPhonebook):
								case 0: EraseRecentCallList = False
								case _: print("Invalid")
				
				
					case 5:
						callduration = True
						while(callduration): 
							print("Show call duration")
				
							message = """
				
							1: Last call duration
							2: All calls' duration
							3: Received calls' duration
							4: Dialled calls' duration
							5: Clear timers
							0: Back
							"""
							print(message)
							select = int(input())
				
							match(select):
								case 1:
									Lastcallduration = True
									while(Lastcallduration): 
										print("Last call duration")
										message = """
										0: Back
										"""
										print(message)
										selectPhonebook = int(input())
				
										match(selectPhonebook):
											case 0: Lastcallduration = False
											case _: print("Invalid")
				
				
				
								case 2:
									AllCallDuration = True
									while(AllCallDuration): 
										print("All Call Duration")
										message = """				
										0: Back
										"""
										print(message)
										selectPhonebook = int(input())
				
										match(selectPhonebook):
											case 0: AllCallDuration = False
											case _: print("Invalid")
				
				
				
								case 3:
									ReceivedCallDurations = True
									while(ReceivedCallDurations): 
										print("Received Call Durations")
										message = """				
										0: Back
										"""
										print(message)
										selectPhonebook = int(input())
				
										match(selectPhonebook):
											case 0: ReceivedCallDurations = False
											case _: print("Invalid")
				
				
				
								case 4:
									DialledCallDurations = True
									while(DialledCallDurations): 
										print("Dialled Call Durations")
										message = """				
										0: Back
										"""
										print(message);
										selectPhonebook = int(input())
				
										match(selectPhonebook):
											case 0: DialledCallDurations = False
											case _: print("Invalid")
				
				
				
								case 5:
									ClearTimers = True;
									while(ClearTimers): 
										print("Clear Timer")
										message = """				
										0: Back
										"""
										print(message)
										selectPhonebook = int(input())
				
										match(selectPhonebook):
											case 0: ClearTimers = False
											case _: print("Invalid")
				
				
				
								case 0:
									callduration = False
				
								case _: print("Error Command")
				
				
				
				
				
					case 6:
						Showcallcost = True
						while(Showcallcost): 
							print("Show call costs")
				
							message = """
				
							1: Last call cost
							2: All calls' cost
							3: Clear counters
							0: Back
							"""
							print(message)
							select = int(input())
				
							match(select):
								case 1:
									Lastcallcost = True
									while(Lastcallcost): 
										print("Last call cost")
										message = """				
										0: Back
										"""
										print(message)
										selectPhonebook = int(input())
				
										match(selectPhonebook):
											case 0: Lastcallcost = False
				
				
											case _: print("Invalid")
				
				
				
								case 2:
									Allcallcost = True
									while(Allcallcost): 
										print("WAll call cost")
										message = """				
										0: Back
										"""
										print(message);
										selectPhonebook = int(input())
				
										match(selectPhonebook):
											case 0: Allcallcost = False
											case _: print("Invalid")
				
			
				
								case 3:
									Clearcounter = True
									while(Clearcounter): 
										print("Clear counter")
										message = """				
										0: Back
										"""
										print(message)
										selectPhonebook = int(input())
				
										match(selectPhonebook):
											case 0: Clearcounter = False
											case _: print("Invalid")
				
				
				
				
								case 0:
									Showcallcost = False
				
								case _: print("Error command")
				
				
				
				
				
				
					case 7:
						Callcostsettings = True
						while(Callcostsettings): 
							print("Call cost settings")
				
							message = """
				
							1: Call cost limit
							2: Show costs in
							0: Back
							"""
							print(message);
							select = int(input())
				
							match(select):
								case 1:
									Callcostlimit = True
									while(Callcostlimit): 
										print("Call cost limit")
										message = """				
										0: Back
										"""
										print(message)
										selectPhonebook = int(input())
				
										match(selectPhonebook):
											case 0: Callcostlimit = False
											case _: print("Invalid")
				
				
				
								case 2:
									CostIn = True
									while(CostIn): 
										print("Cost In")
										message = """
										press a number:
				
										0: Back
				
										"""
										print(message)
										selectPhonebook = int(input())
				
										match(selectPhonebook):
											case 0: CostIn = False
											case _: print("Invalid")
				
				
				
				
								case 0:
									Callcostsettings = False
				
								case _: print("Error Command")
				
				
				
				
				
				
					case 8:
						PrepaidCredit = True
						while(PrepaidCredit): 
							print("Welcome to Prepaid Credit")
							message = """
							0: Back
							"""
							print(message)
							selectPhonebook = int(input())

							match(selectPhonebook):
								case 0: PrepaidCredit = False
								case _: print("Invalid")



				
				
					case 0:
						Callregister = False
				
					case _: print("Error command")

		case 5:
			Tone = True
			while(Tone): 
				print("Tone")
				message = """
			
				1: Ringing tone
				2: Ringing volume
				3: Incoming call alert
				4: Composer
				5: Message alert tone
				6: Keypad tones
				7: Warning and game tones
				8: Viberating alert
				9: Screen saver
				0: Back
				""";
				print(message)
				select = int(input())
			
				match(select):
			
					case 1:
						Ringingtone = True
						while(Ringingtone): 
							print("Ringing tone")
							message = """			
							0: Back
							"""
							print(message)
							selectPhonebook = int(input())
			
							match(selectPhonebook):
								case 0: Ringingtone = False
								case _: print("Invalid")
			
					case 2:
						RingingVolume = True
						while(RingingVolume): 
							print("Ringing Volume")
							message = """			
							0: Back
							"""
							print(message)
							selectPhonebook = int(input())
			
							match(selectPhonebook):
								case 0: RingingVolume = False
								case _: print("Invalid")
			
					case 3:
						IncomingCallAlert = True
						while(IncomingCallAlert): 
							print("Incoming Call Alert")
							message = """
							0: Back
							"""
							print(message)
							selectPhonebook = int(input())
			
							match(selectPhonebook):
								case 0: IncomingCallAlert = False
								case _: print("Invalid")
			
			
			
					case 4:
						Composer = True
						while(Composer): 
							print("Composer")
							message = """			
							0: Back
							"""
							print(message)
							selectPhonebook = int(input())
			
							match(selectPhonebook):
								case 0: Composer = False
			
			
								case _: print("Invalid")
			
			
					case 5:
						MessageAlertTone = True
						while(MessageAlertTone): 
							print("Message Alert Tone")
							message = """
							0: Back
							"""
							print(message)
							selectPhonebook = int(input())
			
							match(selectPhonebook):
								case 0: MessageAlertTone = False
								case _: print("Invalid")
			
					case 6:
						KeypadTone = True
						while(KeypadTone): 
							print("Keypad Tone")
							message = """			
							0: Back
							"""
							print(message)
							selectPhonebook = int(input())
			
							match(selectPhonebook):
								case 0: KeypadTone = False
								case _: print("Invalid")
			
					case 7:
						WarningAndGameTone = True
						while(WarningAndGameTone): 
							print("Warning And Game Tone")
							message = """			
							0: Back
							"""
							print(message)
							selectPhonebook = int(input())
			
							match(selectPhonebook):
								case 0: WarningAndGameTone = False
								case _: print("Invalid")
			
					case 8:
						VibratingTone = True
						while(VibratingTone): 
							print("Vibrating Tone")
							message = """			
							0: Back
							"""
							print(message)
							selectPhonebook = int(input())
			
							match(selectPhonebook):
								case 0: VibratingTone = False
								case _: print("Invalid")
			
			
					case 9:
						ScreenSaver = True
						while(ScreenSaver): 
							print("Screen Saver")
							message = """			
							0: Back
							"""
							print(message)
							selectPhonebook = int(input())
			
							match(selectPhonebook):
								case 0: ScreenSaver = False
								case _: print("Invalid")
			

					case 0:
						Tone = False
			
					case _: print("Error Command")

		case 6:
			Settings = True
			while(Settings): 
			
				print("Settings")
			
				message = """
			
				1: Call Settings
				2: Phone settings
				3: Security settings
				4: Restore factory settings
				0: Back

				"""
				print(message);
				select = int(input())
			
				match(select):
			
					case 1:
						CallSettings = True
						while(CallSettings): 
							print("Call Settings")
			
							message = """
							1: Automatic redial
							2: Speed dialing
							3: Call waiting options
							4: Own number sending
							5: Phone line in use
							6: Automatic answer
							0: Back
							"""
							print(message)
							select = int(input())
			
							match(select):
			
								case 1:
									AutomaticRedial = True
									while(AutomaticRedial): 
										print("Automatic Redial")
										message = """			
										0: Back
										"""
										print(message)
										selectPhonebook = int(input())
			
										match(selectPhonebook):
											case 0: AutomaticRedial = False
											case _: print("Invalid")
			
			
			
								case 2:
									Speeddialling = True
									while(Speeddialling): 
										print("Speed dialling")
										message = """			
										0: Back
										"""
										print(message)
										selectPhonebook = int(input())
			
										match(selectPhonebook):
											case 0: Speeddialling = False
											case _: print("Invalid")
			
			
			
								case 3:
									Callwaitingoption = True
									while(Callwaitingoption): 
										print("Call waiting option")
										message = """
										0: Back
										"""
										print(message);
										selectPhonebook = int(input())
			
										match(selectPhonebook):
											case 0: Callwaitingoption = False
											case _: print("Invalid")
			
			
			
								case 4:
									Ownnumbersending = True
									while(Ownnumbersending): 
										print("Own number sending")
										message = """
										0: Back
										"""
										print(message)
										selectPhonebook = int(input())
			
										match(selectPhonebook):
											case 0: Ownnumbersending = False
											case _: print("Invalid")
			
								case 5:
									Phonelineinuse = True
									while(Phonelineinuse): 
										print("Phone line in use")
										message = """			
										0: Back
										"""
										print(message)
										selectPhonebook = int(input())
			
										match(selectPhonebook):
											case 0: Phonelineinuse = False
											case _: print("Invalid")			
			
								case 6:
									AutomaticAnswer = True
									while(AutomaticAnswer): 
										print("Automatic Answer")
										message = """			
										0: Back
										"""
										print(message)
										selectPhonebook = int(input())
			
										match(selectPhonebook):
											case 0: AutomaticAnswer = False
											case _: print("Invalid")
			
								case 0:
									CallSettings = False
			
								case _: print("Error Command")
			
					case 2:
						PhoneSettings = True
						while(PhoneSettings): 
							print("Phone settings")
			
							message = """			
							1: Language
							2: Cell info display
							3: Welcome note
							4: Network selection
							5: Lights
							6: Confirm SIM service action
							0: Back
							"""
							print(message)
							select = int(input())
			
							match(select):
			
								case 1:
									Language = True
									while(Language): 
										print("Language")
										message = """			
										0: Back
										"""
										print(message)
										selectPhonebook = int(input())
			
										match(selectPhonebook):
											case 0: Language = False	
											case _: print("Invalid")
			
								case 2:
									CellinfoDisplay = True
									while(CellinfoDisplay): 
										print("Cell info Display")
										message = """			
										0: Back
										"""
										print(message)
										selectPhonebook = int(input())
			
										match(selectPhonebook):
											case 0: CellinfoDisplay = False
											case _: print("Invalid")
			
								case 3:
									WelcomeNote = True
									while(WelcomeNote): 
										print("Note")
										message = """			
										0: Back
										"""
										print(message);
										selectPhonebook = int(input())
			
										match(selectPhonebook):
											case 0: WelcomeNote = false;
											case _: print("Invalid")
			
								case 4:
									NetworkSelection = True
									while(NetworkSelection): 
										print("Network Selection")
										message = """			
										0: Back
										"""
										print(message)
										selectPhonebook = int(input())
			
										match(selectPhonebook):
											case 0: NetworkSelection = False
											case _: print("Invalid")
			
								case 5:
									Lights = True
									while(NetworkSelection): 
										print("Lights")
										message = """			
										0: Back
										"""
										print(message)
										selectPhonebook = int(input())
			
										match(selectPhonebook):
											case 0: Lights = False
											case _: print("Invalid")
			
		
			
			
								case 6:
									SimServiceAction = True
									while(SimServiceAction): 
										print("Confirm Sim Service Action")
										message = """			
										0: Back
										"""
										print(message)
										selectPhonebook = int(input())
			
										match(selectPhonebook):
											case 0: SimServiceAction = False
											case _: print("Invalid")
			
			
			
			
								case 0:
									PhoneSettings = False
				
								case _: print("Error Command")
			
			
			
			
			
			
					case 3:
						SecuritySettings = True
						while(SecuritySettings): 
							print("Security settings")
			
							message = """
			
							1: PIN code request
							2: Call barring service
							3: Fixed dialling
							4: Closed user group
							5: Phone security
							6: Change access codes
							0: Back
							"""
							print(message)
							select = int(input())
			
							match(select):
			
								case 1:
									Pincoderequest = True
									while(Pincoderequest): 
										print("Pin code request")
										message = """			
										0: Back
										"""
										print(message)
										selectPhonebook = int(input())
			
										match(selectPhonebook):
											case 0: Pincoderequest = False
											case _: print("Invalid")
			
			
								case 2:
									Callbarringservice = True
									while(Callbarringservice): 
										print("Call barring service")
										message = """			
										0: Back
										"""
										print(message)
										selectPhonebook = int(input())
			
										match(selectPhonebook):
											case 0: Callbarringservice = False
											case _: print("Invalid")
			
			
			
								case 3:
									Fixeddialling = True
									while(Fixeddialling): 
										print("Fixed dialling")
										message = """			
										0: Back
										"""
										print(message)
										selectPhonebook = int(input())
			
										match(selectPhonebook):
											case 0: Fixeddialling = False
											case _: print("Invalid")
			
			
			
								case 4:
									ClosedUserGroup = True
									while(ClosedUserGroup): 
										print("Closed User Group")
										message = """			
										0: Back
										"""
										print(message)
										selectPhonebook = int(input())
			
										match(selectPhonebook):
											case 0: ClosedUserGroup = False
											case _: print("Invalid")
			
			
			
								case 5:
									Phonesecurity = True
									while(Phonesecurity): 
										print("Phone security")
										message = """			
										0: Back
										"""
										print(message)
										selectPhonebook = int(input())
			
										match(selectPhonebook):
											case 0: Phonesecurity = False
			
			
											case _: print("Invalid")
			
			
			
								case 6:
									ChangeAccessCode = True
									while(ChangeAccessCode): 
										print("Change Access Code")
										message = """			
										0: Back
										"""
										print(message)
										selectPhonebook = int(input())
			
										match(selectPhonebook):
											case 0: ChangeAccessCode = False
			
			
											case _: print("Invalid")
			
								case 0:
									SecuritySettings = False
			
								case _: print("Error Command")
			
			
			
					case 4:
						Restorefactorysettings = True
						while(Restorefactorysettings): 
							print("Restore factory settings")
							message = """			
							0: Back
							"""
							print(message)
							selectPhonebook = int(input())
			
							match(selectPhonebook):
								case 0: Restorefactorysettings = False
								case _: print("Invalid")			
			
					case 0:
						Settings = False
			
					case _: print("Error Command")
			


		case 7:
			CallDivert = True
			while(CallDivert): 
				print("Call Divert")
				message = """			
				0: Back
				"""
				print(message);
				selectPhonebook = int(input())
			
				match(selectPhonebook):
					case 0: CallDivert = False
					case _: print("Invalid")
			


		case 8:
			Games = True
			while(Games): 
				print("Games")
				message = """			
				0: Back
			
				"""
				print(message);
				selectPhonebook = int(input())
			
				match(selectPhonebook):
					case 0: Games = False
					case _: print("Invalid")
			


		case 9:
			Calculator = True
			while(Calculator): 
				print("Calculator")
				message = """			
				0: Back
				"""
				print(message)
				selectPhonebook = int(input())
			
				match(selectPhonebook):
					case 0: Calculator = False
					case _: print("Invalid")
			


		case 10:
			Remainders = True
			while(Remainders): 
				print("Remainders")
				message = """			
				0: Back
				"""
				print(message);
				selectPhonebook = int(input())
			
				match(selectPhonebook):
					case 0: Remainders = False
			
			
					case _: print("Invalid")
		case 11:
			Clock = True
			while(Clock): 
				print("Clock")
			
				message = """
			
				1: Alarm clock
				2: Clock settings
				3: Date settings
				4: Stopwatch
				5: Countdown timer
				6: Auto update of date and time
				0: Back
				"""
				print(message)
				select = int(input())
			
				match(select):
			
					case 1:
						AlarmClock = True
						while(AlarmClock): 
							print("Alarm Clock")
							message = """			
							0: Back
							"""
							print(message)
							selectPhonebook = int(input())
			
							match(selectPhonebook):
								case 0: AlarmClock = False
								case _: print("Invalid")
			
					case 2:
						ClockSetting = True
						while(ClockSetting): 
							print("Clock Setting")
							message = """			
							0: Back
							"""
							print(message)
							selectPhonebook = int(input())
			
							match(selectPhonebook):
								case 0: ClockSetting = False
								case _: print("Invalid")
			
					case 3:
						Datesettings = True
						while(Datesettings): 
							print("Date settings")
							message = """			
							0: Back
							"""
							print(message)
							selectPhonebook = int(input())
			
							match(selectPhonebook):
								case 0: Datesettings = False
								case _: print("Invalid")
		
					case 4:
						StopWatch = True
						while(StopWatch): 
							print("Stop Watch")
							message = """			
							0: Back
							"""
							print(message)
							selectPhonebook = int(input())
			
							match(selectPhonebook):
								case 0: StopWatch = false;
								case _: print("Invalid")
		
					case 5:
						CountdownTimer = True
						while(CountdownTimer): 
							print("Countdown Timer")
							message = """			
							0: Back
							"""
							print(message)
							selectPhonebook = int(input())
			
							match(selectPhonebook):
								case 0: CountdownTimer = False
								case _: print("Invalid")
			
					case 6:
						Autoupdateoftimeanddate = True
						while(Autoupdateoftimeanddate): 
							print("Autoupdate of time and date")
							message = """			
							0: Back
							"""
							print(message)
							selectPhonebook = int(input())
			
							match(selectPhonebook):
								case 0: Autoupdateoftimeanddate = False
								case _: System.out.println("Invalid")
			

					case 0:
						Clock = False
			
					case _: print("Error Command")
	
		case 12:
			Profile = True
			while(Profile): 
				print("Profile")
				message = """			
				0: Back
				"""
				print(message);
				selectPhonebook = int(input())
			
				match(selectPhonebook):
					case 0: Profile = False
					case _: print("Invalid")
			
		case 13:
			SimService = True
			while(SimService): 
				print("SimService")
				message = """
				0: Back
				"""
				print(message)
				selectPhonebook = int(input())
			
				match(selectPhonebook):
					case 0: SimService = False
					case _: print("Invalid")
		
		
		case 0: menu = False
		case _: print("Error Command")
			





	



