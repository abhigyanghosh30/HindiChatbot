# data for chatbot
# entries prestructured as layed out in Weizenbaum's description 
# [cf: Communications of the ACM, Vol. 9, #1 (January 1966): p 36-45.]

initials = [
    "namaste. aap kaise hai",
    "kya chal raha hai?",
    "kya aapko koi pareshaani hai"
]

elizaFinals = [
    "bye. aapse mil ke khushi hui"
]

quits = [
  "bye",
  "alvidaa"
]

synons = {
    "parivaar" : ["maa","maataa","pitaa","bhaai","bahan"]
}

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
        ["*",[
            "mujhe samajh nahi aayaa",
            "aur bataaiye",
            "yah dilachasp hai. krpaya jaari rakhe",
            "yah aapako kya sujhaav deta hai?",
        ]]
    ]],
    ["yaad",1,[
        ["^.* yaad rakhnaa .* (.+)* meraa (.+)* se (.+)* tak .*",[
            "def schedule(1,2,3)"
        ]],
        ["^.* yaad rakhnaa .* meraa (.+)* se (.+)* tak .*",[
            "def schedule(1,2,3)"
        ]],
        ["^.* yaad dilaanaa .* meraa (.+)* (.+)* se (.+)* tak .*",[
            "def schedule(1,2,3)"
        ]],
        ["^.* yaad dilaanaa .* (.+)* meraa (.+)* se (.+)* tak .*",[
            "def schedule(1,2,3)"
        ]],
        ["^.* yaad rakhnaa .* (.+)* meraa (.+)* se (.+)* .*",[
            "def schedule(1,2,3)"
        ]],
        ["^.* yaad rakhnaa .* meraa (.+)* se (.+)* .*",[
            "def schedule(1,2,3)"
        ]],
        ["^.* yaad dilaanaa .* meraa (.+)* (.+)* se (.+)* .*",[
            "def schedule(1,2,3)"
        ]],
        ["^.* yaad dilaanaa .* (.+)* meraa (.+)* se (.+)* .*",[
            "def schedule(1,2,3)"
        ]],
    ]],
    ["naam",15,[
        ["(.+)* naam (.+)* hai",[
            "hello {1}"
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

