from collections import deque

printer_queue=deque()
printer_queue.append("TaylarSwiftTcikets.pdf")
printer_queue.append("MarketingNotes.docx")
printer_queue.append("proof.png")

while len(printer_queue)>0:
    document=printer_queue.popleft()
    print(f'Pringting {document}')