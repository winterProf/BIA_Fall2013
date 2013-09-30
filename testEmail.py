import re
# from parse_solution import parse_email

def parse_email(str):
    """ returns a dictionary with 'user','domain','tld' """
    """ ex: {'user':'wmason','domain':'stevens','tld':'edu'} """
    """ or empty dictionary if not valid """
    solution = {}
    match_string = '''
		(^| )
		(?P<user>[a-zA-Z0-9_\+\.]+)
		@
		(?P<domain>[a-zA-Z0-9]+)
		\.
		(?P<tld>[a-zA-Z]{2,3})
		( |\.|$)
		'''
    emails = re.compile(match_string)
    match = emails.search(str)
    if match:
        solution['user'] = match.group('user')
        solution['domain'] = match.group('domain')
        solution['tld'] = match.group('tld')
    
    return solution


if __name__=="__main__":
    print "Beginning tests"
    assert(parse_email("@twitter handle")=={})
    assert(parse_email("not.valid@domain")=={})
    assert(parse_email("domain@valid.butnotreally")=={})
    assert(parse_email("This&isn't@right.com")=={})
    assert(parse_email("not=valid@domain.com")=={})
    assert(parse_email("also@not@valid@domain.com")=={})
    assert(parse_email("me@google.com")=={'user':'me','domain':'google','tld':'com'})
    assert(parse_email("ME@YAHOO.COM")=={'user':'ME','domain':'YAHOO','tld':'COM'})
    assert(parse_email("WINTER.MASON@YAHOO.COM")=={'user':'WINTER.MASON','domain':'YAHOO','tld':'COM'})
    assert(parse_email("winter.mason@yahoo.com")=={'user':'winter.mason','domain':'yahoo','tld':'com'})
    assert(parse_email("this is a test me@example.com")=={'user':'me','domain':'example','tld':'com'})
    assert(parse_email("this is a harder test me@example.com.")=={'user':'me','domain':'example','tld':'com'})
    assert(parse_email("An email in context me@example.com is hard.")=={'user':'me','domain':'example','tld':'com'})
    assert(parse_email("alpha123@google.com")=={'user':'alpha123','domain':'google','tld':'com'})
    assert(parse_email("alpha.123@google.com")=={'user':'alpha.123','domain':'google','tld':'com'})
    assert(parse_email("123@google.com")=={'user':'123','domain':'google','tld':'com'})
    assert(parse_email("under_score@mail.edu")=={'user':'under_score','domain':'mail','tld':'edu'})
    assert(parse_email("h@bit.ly")=={'user':'h','domain':'bit','tld':'ly'})
    assert(parse_email("oddly+@mail.com")=={'user':'oddly+','domain':'mail','tld':'com'})
    assert(parse_email("rb@check.io")=={'user':'rb','domain':'check','tld':'io'})
    print "All tests passed!"

