# Mr-Worldwide

## Problem

A musician left us a [message](https://jupiter.challenges.picoctf.org/static/d5570d48262dbba2a31f2a940409ad9d/message.txt). What's it mean?

## Links

* [message](https://jupiter.challenges.picoctf.org/static/d5570d48262dbba2a31f2a940409ad9d/message.txt)

## Notes

The name message looks to be a bunch of x and 7 coordinates.  The challange name "Mr. Worldwide" makes me think these are global coordinates, but the musician comment might make it something to do with musical notation.

Here is the message

```text
picoCTF{(35.028309, 135.753082)(46.469391, 30.740883)(39.758949, -84.191605)(41.015137, 28.979530)(24.466667, 54.366669)(3.140853, 101.693207)_(9.005401, 38.763611)(-3.989038, -79.203560)(52.377956, 4.897070)(41.085651, -73.858467)(57.790001, -152.407227)(31.205753, 29.924526)}
```


Breaking the coordinates down into their locations, Google maps is useful for this, just pasting in the coordinates shows the locations

```text
(35.028309, 135.753082) Nakanocho, Kamigyo Ward, Kyoto, 602-0958, Japan
(46.469391, 30.740883) Odesa, Odessa Oblast, Ukraine, 65000
(39.758949, -84.191605) Dayton, OH 45402
(41.015137, 28.979530) Hoca Paşa, 34110 Fatih/İstanbul, Turkey
(24.466667, 54.366669) Hazza ' Bin Zayed The First St - Al Manhal - Abu Dhabi - United Arab Emirates
(3.140853, 101.693207) Room 11, Level 2, Bangunan Sulaiman, Jalan Sultan Hishamuddin, 50000 Kuala Lumpur, Malaysia
_
(9.005401, 38.763611)  Kirkos, Addis Ababa, Ethiopia
(-3.989038, -79.203560)  Av. Nueva Loja, Loja, Ecuador
(52.377956, 4.897070) Martelaarsgracht 5, 1012 TM Amsterdam, Netherlands
(41.085651, -73.858467)   Sleepy Hollow, NY 10591
(57.790001, -152.407227)  Kodiak, AK 99615
(31.205753, 29.924526) Faculty Of Engineering, Al Azaritah WA Ash Shatebi, Bab Sharqi, Alexandria Governorate 5423021, Egypt
```

Seems the flag is made up of larger cities or regions instead of the exact location.

```txt
[K]yoto             (35.028309, 135.753082)
[O]dessa            (46.469391, 30.740883)
[D]ayton            (39.758949, -84.191605)
[I]stanbul          (41.015137, 28.979530)
[A]bu Dhabi         (24.466667, 54.366669)
[K]uala Lumpur      (3.140853, 101.693207)
_
[A]ddis Ababa       (9.005401, 38.763611)
[L]oja              (-3.989038, -79.203560)
[A]msterdam         (52.377956, 4.897070)
[S]leepy Hollow     (41.085651, -73.858467)
[K]odiak            (57.790001, -152.407227)
[A]lexandria        (31.205753, 29.924526)
---------------------------------------------
picoCTF{KODIAK_ALASKA}
``` 

## Solution

The flag is made up of city and region locations shown in the table above.  The flag is picoCTF{KODIAK_ALASKA}

