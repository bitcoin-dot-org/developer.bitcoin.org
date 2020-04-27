# Distributed under the MIT software license, see the accompanying
# file LICENSE or https://www.opensource.org/licenses/MIT.

# List of words which are recognized in commands. The display_name method
# also recognizes strings between these words as own words so not all words
# appearing in command names have to be listed here but only enough to separate
# all words.
#
# Keep the list ordered alphabetically so it's easier for a developer to see if
# a word already is there
word_list = ["abort", "account", "address", "balance", "block", "by", "chain",
             "change", "clear", "connection", "convert", "decode",
             "fee", "generate", "get", "hash", "header",
             "import", "info", "key", "label",
             "message", "multi", "network", "node", "out", "psbt", "pool",
             "priv", "pruned", "list", "raw", "save", "send", "smart", "totals",
             "transaction", "tx", "unspent", "wallet",
             ]

# List of explicit display names which would otherwise wrongly generated from
# the word list
explicit_display_names = {
    "setban": "SetBan",
    "listaccounts": "ListAccounts",
    "listwallets": "ListWallets",
    "listtransactions": "ListTransactions",
    "sethdseed": "SetHdSeed",
    "getaddressesbylabel": "GetAddressesByLabel",
    "getaddressesbyaccount": "GetAddressesByAccount",
    "getnodeaddresses": "GetNodeAddresses",
    "joinpsbts": "JoinPsbts",
    "utxoupdatepsbt": "UtxoUpdatePsbt",
    "deriveaddresses": "DeriveAddresses",
    "listlabels": "ListLabels",
}


def capitalize(word):
    if len(word) > 1:
        return word[0].upper() + word[1:]
    else:
        return word.upper()


def uncapitalize(word):
    if len(word) > 1:
        return word[0].lower() + word[1:]
    else:
        return word.lower()


def display_name(command):
    if command in explicit_display_names:
        return explicit_display_names[command]

    name = ""
    last_word_index = 0
    i = 0
    while i < len(command):
        found_word = False
        for word in word_list:
            if command[i:i+len(word)] == word:
                if last_word_index < i:
                    name += capitalize(command[last_word_index:i])
                name += capitalize(word)
                i += len(word)
                last_word_index = i
                found_word = True
                break
        if not found_word:
            i += 1
    if last_word_index < i:
        name += capitalize(command[last_word_index:i])
    return capitalize(name)
