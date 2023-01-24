def lucky(ticket):
    global lastTicket
    lastTicket_numbers = [int(x) for x in str(lastTicket)]
    ticket_numbers = [int(x) for x in str(ticket)]
    if sum(lastTicket_numbers[:len(lastTicket_numbers) // 2]) == sum(lastTicket_numbers[len(lastTicket_numbers) // 2:]) \
            and sum(ticket_numbers[:len(ticket_numbers) // 2]) == sum(ticket_numbers[len(ticket_numbers) // 2:]):
        return 'Счастливый'
    else:
        return 'Несчастливый'


# lastTicket = 123456
# print(lucky(100001))
# lastTicket = 123321
# print(lucky(100001))
# lastTicket = 111111
# print(lucky(2020))
