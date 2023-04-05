```
Possible ways of parcing grpc.
```

---


**Me:**
how to parse data from network tab when you are do not have access to server and frontend uses grpc to communicate with backend

---

**Me:**
If you do not have access to the server and the frontend uses gRPC to communicate with the backend, it may be difficult to directly access the network tab to parse the data. However, there are a few possible ways to try to capture and analyze the network traffic:
<li>Use a network packet capture tool: You can use a tool such as Wireshark to capture the network traffic on your local machine. This will allow you to see the network packets being sent and received by your machine, even if you don't have access to the server. You can then filter the captured packets to show only those related to the gRPC traffic and analyze the data.</li><li>Use a proxy server: You can set up a proxy server between the frontend and backend to intercept the network traffic. This will allow you to capture the data being sent and received by the frontend and backend. You can then analyze this data to extract the information you need.</li><li>Use a debugging tool: Some programming languages and frameworks have built-in debugging tools that allow you to inspect network traffic. For example, if the frontend is written in JavaScript, you can use the Chrome Developer Tools to inspect network traffic. Similarly, if the backend is written in Java, you can use tools such as Java VisualVM or JConsole to inspect network traffic.</li>
Keep in mind that capturing network traffic without proper authorization may be illegal and could have serious consequences. Make sure to obtain permission before attempting to capture network traffic.

---

**Me:**
so how could i properly found data without protobuf file 

---

**Me:**
If you don't have access to the protobuf file, it may be more difficult to parse the data from the network tab. The protobuf file provides a schema that defines the structure of the messages being sent and received, which makes it easier to decode the data.
Without the protobuf file, you may need to use a reverse engineering approach to try to understand the structure of the messages. Here are some steps you could take:
<li>Analyze the network traffic: Use a network capture tool such as Wireshark to capture the network traffic between the frontend and backend. Look for messages that are being sent and received and try to identify any patterns in the data.</li><li>Identify message headers: Look for headers or metadata in the messages that may provide clues about the structure of the data. For example, some gRPC messages may include a "message type" field that indicates the type of message being sent.</li><li>Analyze message payloads: Look at the payload of each message to try to identify any patterns or structures. You may need to do some trial and error to figure out the structure of the data.</li><li>Use a tool to decode the data: Once you have a better understanding of the structure of the data, you can use a tool such as a hex editor or a custom script to decode the data. This will allow you to extract the information you need.</li>
Keep in mind that reverse engineering can be a time-consuming and challenging process, and it may not be possible to decode all of the data without the protobuf file. If possible, try to obtain the protobuf file from the backend developers to make the decoding process easier.

---

**Me:**
thank you for your honest answer

---

**Me:**
You're welcome! If you have any further questions or concerns, feel free to ask.
