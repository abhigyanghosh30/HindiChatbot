# data for chatbot
# entries prestructured as layed out in Weizenbaum's description 
# [cf: Communications of the ACM, Vol. 9, #1 (January 1966): p 36-45.]

initials = [
    "namaste. aap kaise hai",
    "kya chal raha hai?",
    "kya aapko koi pareshaani hai?",
    "mai aapki kaise madad kar sakta hoon?"
]

elizaFinals = [
    "bye. aapse mil ke khushi hui"
]

quits = [
  "bye",
  "alvidaa"
]

# synons = {
#     "parivaar" : ["maa","maataa","pitaa","bhaai","bahan"]
# }

# Keywords
# Array of
#   ["<key>", <rank>, [
#     ["<decomp>", [
#       "<reasmb>",
#       "<reasmb>",
#       "<reasmb>"
#     ]],
#     ["<decomp>", [
#       "<reasmb>",
#       "<reasmb>",
#       "<reasmb>"
#     ]]
#   ]]

keywords = [
    ["xnone",0,[
        ["^.*",[
            "mujhe samajh nahi aayaa",
        ]]
    ]],
    ["yaad",6,[
        ["^.* yaad rakhnaa .* (.+)* meraa (.+)* se (.+)* tak (.+)* .*",[
            "def schedule()"
        ]],
        ["^.* yaad rakhnaa .* meraa (.+)* se (.+)* tak (.+)* .*",[
            "def schedule()"
        ]],
        ["^.* yaad dilaanaa .* meraa (.+)* (.+)* se (.+)* tak (.+)* .*",[
            "def schedule()"
        ]],
        ["^.* yaad dilaanaa .* (.+)* meraa (.+)* se (.+)* tak (.+)* .*",[
            "def schedule()"
        ]],
        ["^.* yaad rakhnaa .* (.+)* meraa (.+)* se (.+)* (.+)* .*",[
            "def schedule()"
        ]],
        ["^.* yaad rakhnaa .* meraa (.+)* se (.+)* (.+)* .*",[
            "def schedule()"
        ]],
        ["^.* yaad dilaanaa .* meraa (.+)* (.+)* se (.+)* (.+)* .*",[
            "def schedule()"
        ]],
        ["^.* yaad dilaanaa .* (.+)* meraa (.+)* se (.+)* (.+)* .*",[
            "def schedule()"
        ]],
    ]],
    ["naam",4,[
        ["(.+)* naam kyaa hai?",[
            "meraa koi naam nahi hai"
        ]],
        ["(.+)* naam (.+)* hai",[
            "hello {s[1]}",
            "ok so?"
        ]],
        ["(.+) (.+)*",[
            "naam mein kyaa rakhaa hai? aago batao"
        ]],
    ]],
    ["mujhe",2,[
        ["^mujhe (.+)* kyaa karnaa hai",[
            "def readout()"
        ]],
        ["^mujhe (.+)* kyaa kyaa karnaa hai",[
            "def readout()"
        ]],
    ]],
    ["meraa", 1,[
        ["meraa (.+)*",[
            "accha? aapka {s[0]}"
        ]],
    ]],
    ["schedule",5,[
        ["^.* (.+)* ka schedule .*",[
            "def readout()"
        ]]
    ]],
    ["kyaa",2,[
        ["kyaa aapko (.+)*",[
            "mujhe {s[0]}"
        ]],
        ["aapko kyaa (.+)*",[
            "mujhe {s[0]}"
        ]],
        ["kyaa tumhe (.+)*",[
            "mujhe {s[0]}"
        ]],
        ["tumhe kyaa (.+)*",[
            "mujhe {s[0]}"
        ]],
    ]]


]

