
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftDOENDANDORIFELSEFORTRUEFALSEFOREXPRNAMEleftEQUALSCONSTANTCHARINTSTRINGDOUBLEleftGREATERLESSGREATEQLESSEQleftPLUSMINUSleftTIMESDIVIDEleftPARENLPARENRrightUMINUSAND CHAR CONSTANT DEF DIVIDE DO DOUBLE ELSE END EQUALS FALSE FOR FOREXPR GREATEQ GREATER IF INT LESS LESSEQ MINUS NAME OR PARENL PARENR PLUS STRING TIMES TRUEstatements : statements statement\n        | statement\n        | expressionstatement : CONSTANT expression\n                 statement : NAME EQUALS expression\n                 | NAME EQUALS expression PARENL expression PARENR\n                 statement : DEF NAME PARENL NAME PARENR DO new_scope statements end_scope END\n                 | DEF NAME PARENL empty PARENR DO new_scope statements end_scope END\n                 | DEF NAME DO new_scope statements end_scope ENDstatement : new_scope if_statement end_scopeif_statement : IF expression DO statements END\n                 | IF expression DO statements ELSE statements END\n                 statement : FOR NAME FOREXPR NAME DO new_scope statements end_scope ENDexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression TIMES expression\n                  | expression DIVIDE expression\n                  | expression GREATER expression\n                  | expression LESS expression\n                  | expression GREATEQ expression\n                  | expression LESSEQ expression\n                  | expression AND expression\n                  | expression OR expression\n                  expression : MINUS expression %prec UMINUSexpression : PARENL new_scope expression end_scope PARENRexpression : INTexpression : DOUBLEexpression : CHARexpression : TRUEexpression : FALSEexpression : STRINGexpression : NAMEempty :new_scope : empty end_scope : empty'
    
_lr_action_items = {'DO':([2,4,7,13,15,16,18,22,23,43,47,48,49,50,51,52,53,54,55,56,61,65,66,69,],[-28,-29,-31,-30,-26,-27,-32,-24,39,60,-22,-23,-17,-20,-19,-16,-21,-14,-15,-18,68,73,74,-25,]),'CONSTANT':([0,2,3,4,7,9,10,13,14,15,16,17,18,19,21,22,24,39,41,42,46,47,48,49,50,51,52,53,54,55,56,57,60,64,67,68,69,73,74,75,76,77,78,79,80,81,82,83,84,85,86,90,91,92,],[1,-28,1,-29,-31,-2,-34,-30,-32,-26,-27,-3,-32,-4,-1,-24,-33,-33,-35,-10,-5,-22,-23,-17,-20,-19,-16,-21,-14,-15,-18,1,1,1,1,-33,-25,-33,-33,-11,1,1,-6,-9,1,1,1,1,1,1,-12,-13,-7,-8,]),'LESS':([2,4,7,13,14,15,16,17,18,19,22,43,45,46,47,48,49,50,51,52,53,54,55,56,69,70,],[-28,-29,-31,-30,-32,-26,-27,33,-32,33,-24,33,33,33,33,33,-17,-20,-19,-16,-21,-14,-15,-18,-25,33,]),'CHAR':([0,1,5,10,12,25,27,28,29,30,31,32,33,34,35,36,37,38,39,57,60,63,68,73,74,76,77,80,81,],[2,2,2,-34,-33,2,2,2,2,2,2,2,2,2,2,2,2,2,-33,2,2,2,-33,-33,-33,2,2,2,2,]),'FOREXPR':([26,],[44,]),'GREATER':([2,4,7,13,14,15,16,17,18,19,22,43,45,46,47,48,49,50,51,52,53,54,55,56,69,70,],[-28,-29,-31,-30,-32,-26,-27,38,-32,38,-24,38,38,38,38,38,-17,-20,-19,-16,-21,-14,-15,-18,-25,38,]),'TRUE':([0,1,5,10,12,25,27,28,29,30,31,32,33,34,35,36,37,38,39,57,60,63,68,73,74,76,77,80,81,],[4,4,4,-34,-33,4,4,4,4,4,4,4,4,4,4,4,4,4,-33,4,4,4,-33,-33,-33,4,4,4,4,]),'MINUS':([0,1,2,4,5,7,10,12,13,14,15,16,17,18,19,22,25,27,28,29,30,31,32,33,34,35,36,37,38,39,43,45,46,47,48,49,50,51,52,53,54,55,56,57,60,63,68,69,70,73,74,76,77,80,81,],[5,5,-28,-29,5,-31,-34,-33,-30,-32,-26,-27,37,-32,37,-24,5,5,5,5,5,5,5,5,5,5,5,5,5,-33,37,37,37,37,37,-17,37,37,-16,37,-14,-15,37,5,5,5,-33,-25,37,-33,-33,5,5,5,5,]),'DEF':([0,2,3,4,7,9,10,13,14,15,16,17,18,19,21,22,24,39,41,42,46,47,48,49,50,51,52,53,54,55,56,57,60,64,67,68,69,73,74,75,76,77,78,79,80,81,82,83,84,85,86,90,91,92,],[6,-28,6,-29,-31,-2,-34,-30,-32,-26,-27,-3,-32,-4,-1,-24,-33,-33,-35,-10,-5,-22,-23,-17,-20,-19,-16,-21,-14,-15,-18,6,6,6,6,-33,-25,-33,-33,-11,6,6,-6,-9,6,6,6,6,6,6,-12,-13,-7,-8,]),'STRING':([0,1,5,10,12,25,27,28,29,30,31,32,33,34,35,36,37,38,39,57,60,63,68,73,74,76,77,80,81,],[7,7,7,-34,-33,7,7,7,7,7,7,7,7,7,7,7,7,7,-33,7,7,7,-33,-33,-33,7,7,7,7,]),'PLUS':([2,4,7,13,14,15,16,17,18,19,22,43,45,46,47,48,49,50,51,52,53,54,55,56,69,70,],[-28,-29,-31,-30,-32,-26,-27,36,-32,36,-24,36,36,36,36,36,-17,36,36,-16,36,-14,-15,36,-25,36,]),'$end':([2,3,4,7,9,13,14,15,16,17,18,19,21,22,24,41,42,46,47,48,49,50,51,52,53,54,55,56,69,75,78,79,86,90,91,92,],[-28,0,-29,-31,-2,-30,-32,-26,-27,-3,-32,-4,-1,-24,-33,-35,-10,-5,-22,-23,-17,-20,-19,-16,-21,-14,-15,-18,-25,-11,-6,-9,-12,-13,-7,-8,]),'PARENR':([2,4,7,13,15,16,18,22,40,41,45,47,48,49,50,51,52,53,54,55,56,58,59,62,69,70,],[-28,-29,-31,-30,-26,-27,-32,-24,-33,-35,-33,-22,-23,-17,-20,-19,-16,-21,-14,-15,-18,65,66,69,-25,78,]),'END':([2,4,7,9,13,14,15,16,17,18,19,21,22,24,41,42,46,47,48,49,50,51,52,53,54,55,56,64,67,69,71,72,75,78,79,82,83,84,85,86,87,88,89,90,91,92,],[-28,-29,-31,-2,-30,-32,-26,-27,-3,-32,-4,-1,-24,-33,-35,-10,-5,-22,-23,-17,-20,-19,-16,-21,-14,-15,-18,-33,75,-25,79,-35,-11,-6,-9,86,-33,-33,-33,-12,90,91,92,-13,-7,-8,]),'DIVIDE':([2,4,7,13,14,15,16,17,18,19,22,43,45,46,47,48,49,50,51,52,53,54,55,56,69,70,],[-28,-29,-31,-30,-32,-26,-27,31,-32,31,-24,31,31,31,31,31,-17,31,31,-16,31,31,31,31,-25,31,]),'FOR':([0,2,3,4,7,9,10,13,14,15,16,17,18,19,21,22,24,39,41,42,46,47,48,49,50,51,52,53,54,55,56,57,60,64,67,68,69,73,74,75,76,77,78,79,80,81,82,83,84,85,86,90,91,92,],[11,-28,11,-29,-31,-2,-34,-30,-32,-26,-27,-3,-32,-4,-1,-24,-33,-33,-35,-10,-5,-22,-23,-17,-20,-19,-16,-21,-14,-15,-18,11,11,11,11,-33,-25,-33,-33,-11,11,11,-6,-9,11,11,11,11,11,11,-12,-13,-7,-8,]),'EQUALS':([14,20,],[28,28,]),'TIMES':([2,4,7,13,14,15,16,17,18,19,22,43,45,46,47,48,49,50,51,52,53,54,55,56,69,70,],[-28,-29,-31,-30,-32,-26,-27,34,-32,34,-24,34,34,34,34,34,-17,34,34,-16,34,34,34,34,-25,34,]),'ELSE':([2,4,7,9,13,14,15,16,17,18,19,21,22,24,41,42,46,47,48,49,50,51,52,53,54,55,56,67,69,75,78,79,86,90,91,92,],[-28,-29,-31,-2,-30,-32,-26,-27,-3,-32,-4,-1,-24,-33,-35,-10,-5,-22,-23,-17,-20,-19,-16,-21,-14,-15,-18,76,-25,-11,-6,-9,-12,-13,-7,-8,]),'PARENL':([0,1,2,4,5,7,10,12,13,15,16,18,22,23,25,27,28,29,30,31,32,33,34,35,36,37,38,39,46,47,48,49,50,51,52,53,54,55,56,57,60,63,68,69,73,74,76,77,80,81,],[12,12,-28,-29,12,-31,-34,-33,-30,-26,-27,-32,-24,40,12,12,12,12,12,12,12,12,12,12,12,12,12,-33,63,-22,-23,-17,-20,-19,-16,-21,-14,-15,-18,12,12,12,-33,-25,-33,-33,12,12,12,12,]),'IF':([0,2,3,4,7,8,9,10,13,14,15,16,17,18,19,21,22,24,39,41,42,46,47,48,49,50,51,52,53,54,55,56,57,60,64,67,68,69,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,90,91,92,],[-33,-28,-33,-29,-31,25,-2,-34,-30,-32,-26,-27,-3,-32,-4,-1,-24,-33,-33,-35,-10,-5,-22,-23,-17,-20,-19,-16,-21,-14,-15,-18,-33,-33,-33,-33,-33,-25,-34,-33,-33,-11,-33,-33,-6,-9,-33,-33,-33,-33,-33,-33,-12,-13,-7,-8,]),'AND':([2,4,7,13,14,15,16,17,18,19,22,43,45,46,47,48,49,50,51,52,53,54,55,56,69,70,],[-28,-29,-31,-30,-32,-26,-27,29,-32,29,-24,29,29,29,-22,-23,-17,-20,-19,-16,-21,-14,-15,-18,-25,29,]),'FALSE':([0,1,5,10,12,25,27,28,29,30,31,32,33,34,35,36,37,38,39,57,60,63,68,73,74,76,77,80,81,],[13,13,13,-34,-33,13,13,13,13,13,13,13,13,13,13,13,13,13,-33,13,13,13,-33,-33,-33,13,13,13,13,]),'NAME':([0,1,2,3,4,5,6,7,9,10,11,12,13,14,15,16,17,18,19,21,22,24,25,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,44,46,47,48,49,50,51,52,53,54,55,56,57,60,63,64,67,68,69,73,74,75,76,77,78,79,80,81,82,83,84,85,86,90,91,92,],[14,18,-28,20,-29,18,23,-31,-2,-34,26,-33,-30,-32,-26,-27,-3,-32,-4,-1,-24,-33,18,18,18,18,18,18,18,18,18,18,18,18,18,-33,58,-35,-10,61,-5,-22,-23,-17,-20,-19,-16,-21,-14,-15,-18,14,14,18,20,20,-33,-25,-33,-33,-11,14,14,-6,-9,14,14,20,20,20,20,-12,-13,-7,-8,]),'GREATEQ':([2,4,7,13,14,15,16,17,18,19,22,43,45,46,47,48,49,50,51,52,53,54,55,56,69,70,],[-28,-29,-31,-30,-32,-26,-27,32,-32,32,-24,32,32,32,32,32,-17,-20,-19,-16,-21,-14,-15,-18,-25,32,]),'INT':([0,1,5,10,12,25,27,28,29,30,31,32,33,34,35,36,37,38,39,57,60,63,68,73,74,76,77,80,81,],[15,15,15,-34,-33,15,15,15,15,15,15,15,15,15,15,15,15,15,-33,15,15,15,-33,-33,-33,15,15,15,15,]),'DOUBLE':([0,1,5,10,12,25,27,28,29,30,31,32,33,34,35,36,37,38,39,57,60,63,68,73,74,76,77,80,81,],[16,16,16,-34,-33,16,16,16,16,16,16,16,16,16,16,16,16,16,-33,16,16,16,-33,-33,-33,16,16,16,16,]),'LESSEQ':([2,4,7,13,14,15,16,17,18,19,22,43,45,46,47,48,49,50,51,52,53,54,55,56,69,70,],[-28,-29,-31,-30,-32,-26,-27,35,-32,35,-24,35,35,35,35,35,-17,-20,-19,-16,-21,-14,-15,-18,-25,35,]),'OR':([2,4,7,13,14,15,16,17,18,19,22,43,45,46,47,48,49,50,51,52,53,54,55,56,69,70,],[-28,-29,-31,-30,-32,-26,-27,30,-32,30,-24,30,30,30,-22,-23,-17,-20,-19,-16,-21,-14,-15,-18,-25,30,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statements':([0,57,60,76,77,80,81,],[3,64,67,82,83,84,85,]),'end_scope':([24,45,64,83,84,85,],[42,62,71,87,88,89,]),'new_scope':([0,3,12,39,57,60,64,67,68,73,74,76,77,80,81,82,83,84,85,],[8,8,27,57,8,8,8,8,77,80,81,8,8,8,8,8,8,8,8,]),'statement':([0,3,57,60,64,67,76,77,80,81,82,83,84,85,],[9,21,9,9,21,21,9,9,9,9,21,21,21,21,]),'if_statement':([8,],[24,]),'expression':([0,1,5,25,27,28,29,30,31,32,33,34,35,36,37,38,57,60,63,76,77,80,81,],[17,19,22,43,45,46,47,48,49,50,51,52,53,54,55,56,17,17,70,17,17,17,17,]),'empty':([0,3,12,24,39,40,45,57,60,64,67,68,73,74,76,77,80,81,82,83,84,85,],[10,10,10,41,10,59,41,10,10,72,10,10,10,10,10,10,10,10,10,72,72,72,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statements","S'",1,None,None,None),
  ('statements -> statements statement','statements',2,'p_expr','parser.py',216),
  ('statements -> statement','statements',1,'p_expr','parser.py',217),
  ('statements -> expression','statements',1,'p_expr','parser.py',218),
  ('statement -> CONSTANT expression','statement',2,'p_assign_cons','parser.py',230),
  ('statement -> NAME EQUALS expression','statement',3,'p_assign_var','parser.py',244),
  ('statement -> NAME EQUALS expression PARENL expression PARENR','statement',6,'p_assign_var','parser.py',245),
  ('statement -> DEF NAME PARENL NAME PARENR DO new_scope statements end_scope END','statement',10,'p_func','parser.py',256),
  ('statement -> DEF NAME PARENL empty PARENR DO new_scope statements end_scope END','statement',10,'p_func','parser.py',257),
  ('statement -> DEF NAME DO new_scope statements end_scope END','statement',7,'p_func','parser.py',258),
  ('statement -> new_scope if_statement end_scope','statement',3,'p_if_scope','parser.py',270),
  ('if_statement -> IF expression DO statements END','if_statement',5,'p_if','parser.py',274),
  ('if_statement -> IF expression DO statements ELSE statements END','if_statement',7,'p_if','parser.py',275),
  ('statement -> FOR NAME FOREXPR NAME DO new_scope statements end_scope END','statement',9,'p_for','parser.py',287),
  ('expression -> expression PLUS expression','expression',3,'p_binary','parser.py',313),
  ('expression -> expression MINUS expression','expression',3,'p_binary','parser.py',314),
  ('expression -> expression TIMES expression','expression',3,'p_binary','parser.py',315),
  ('expression -> expression DIVIDE expression','expression',3,'p_binary','parser.py',316),
  ('expression -> expression GREATER expression','expression',3,'p_binary','parser.py',317),
  ('expression -> expression LESS expression','expression',3,'p_binary','parser.py',318),
  ('expression -> expression GREATEQ expression','expression',3,'p_binary','parser.py',319),
  ('expression -> expression LESSEQ expression','expression',3,'p_binary','parser.py',320),
  ('expression -> expression AND expression','expression',3,'p_binary','parser.py',321),
  ('expression -> expression OR expression','expression',3,'p_binary','parser.py',322),
  ('expression -> MINUS expression','expression',2,'p_minus','parser.py',385),
  ('expression -> PARENL new_scope expression end_scope PARENR','expression',5,'p_group','parser.py',391),
  ('expression -> INT','expression',1,'p_int','parser.py',397),
  ('expression -> DOUBLE','expression',1,'p_double','parser.py',403),
  ('expression -> CHAR','expression',1,'p_char','parser.py',409),
  ('expression -> TRUE','expression',1,'p_true','parser.py',415),
  ('expression -> FALSE','expression',1,'p_false','parser.py',421),
  ('expression -> STRING','expression',1,'p_string','parser.py',427),
  ('expression -> NAME','expression',1,'p_name','parser.py',438),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',461),
  ('new_scope -> empty','new_scope',1,'p_new_scope','parser.py',478),
  ('end_scope -> empty','end_scope',1,'p_end_scope','parser.py',489),
]
