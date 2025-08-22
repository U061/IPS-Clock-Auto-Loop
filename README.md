# IPS-Clock-Auto-Loop
Using EleksTubeIPS firmware , auto loop functionality using python websockets on IPSTUBE.

**Only used Clock and Display option - can add more **

Payload 9:1:time_or_date:0 for Time
Payload 9:1:time_or_date:1 for Date
Payload 9:1:time_or_date:2 for Weather

**Display off**

9:1:display_on:1

9:1:display_on:3


**Display on**

9:1:display_on:1

9:1:display_on:24

**Random Color Values**
9:2:led_hue:20
9:2:led_saturation:10

**Random Brightness Value**
9:2:led_value:255 (Commented out in the code)

**Example Video**

https://github.com/user-attachments/assets/ff1b5454-744a-4796-9741-5d1ece0d6e89

