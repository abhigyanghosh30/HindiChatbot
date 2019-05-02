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
            "aur bataaiye",
            "yah toh badi dilachasp baat hai",
            "yah aapako kya sujhaav deta hai?",
        ]]
    ]],
    ["yaad",1,[
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
    ["naam",15,[
        ["(.+)* naam (.+)* hai",[
            "hello {s[1]}",
            "ok so?"
        ]],
        ["(.+)* naam kya hai?",[
            ""
        ]],
        ["(.+)",[
            "naam mein kya rakha hai? aago batao"
        ]],
    ]],
    ["baat",12,[
        ["",[
            ""
        ]]
    ]]
]

