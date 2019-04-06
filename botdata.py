# data for chatbot
# entries prestructured as layed out in Weizenbaum's description 
# [cf: Communications of the ACM, Vol. 9, #1 (January 1966): p 36-45.]

# Transliteration Index
# अ - a आ - aa इ - i ई - i
# उ - u ऊ - oo ए - e ऐ - ai 
# ओ - o औ - au 
# क - k ख - kh ग - g घ - gh 
# च - ch छ - ch ज - j झ - jh 
# ट - t ठ - th ड - d ढ - dh ण - n 
# त - t थ - th द - d ध - dh न - n
# प - p फ - f ब - b भ - bh म - m 
# य - y र - r ल - l व - v
# श - sh ष - sh स - s ह - h

initials = [
    "namaste. aap kaise hai",
    "kya chal raha hai?",
    "kya aapko koi pareshaani hai"
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
        ]]
    ]]
]

