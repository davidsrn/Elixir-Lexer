
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftDOENDANDORIFELSEFORTRUEFALSEFOREXPRNAMEleftEQUALSCONSTANTCHARINTSTRINGDOUBLEleftGREATERLESSGREATEQLESSEQleftPLUSMINUSleftTIMESDIVIDEleftPARENLPARENRrightUMINUSAND CHAR CONSTANT DEF DIVIDE DO DOUBLE ELSE END EQUALS FALSE FOR FOREXPR GREATEQ GREATER IF INT LESS LESSEQ MINUS NAME OR PARENL PARENR PLUS STRING TIMES TRUEstatements : statements statement\n        | statement\n        | expressionstatement : CONSTANT expression\n                 statement : NAME EQUALS expression\n                 statement : DEF NAME PARENL NAME PARENR DO new_scope statements end_scope END\n                 | DEF NAME PARENL empty PARENR DO new_scope statements end_scope END\n                 | DEF NAME DO new_scope statements end_scope ENDstatement : new_scope if_statement end_scopeif_statement : IF expression DO statements END\n                 | IF expression DO statements ELSE statements END\n                 statement : FOR NAME FOREXPR NAME DO new_scope statements end_scope ENDexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression TIMES expression\n                  | expression DIVIDE expression\n                  | expression GREATER expression\n                  | expression LESS expression\n                  | expression GREATEQ expression\n                  | expression LESSEQ expression\n                  | expression AND expression\n                  | expression OR expression\n                  expression : MINUS expression %prec UMINUSexpression : PARENL new_scope expression end_scope PARENRexpression : INTexpression : DOUBLEexpression : CHARexpression : TRUEexpression : FALSEexpression : STRINGexpression : NAMEempty :new_scope : empty end_scope : empty'
    
_lr_action_items = {'DO':([2,4,7,13,15,16,18,22,23,43,47,48,49,50,51,52,53,54,55,56,61,64,65,68,],[-27,-28,-30,-29,-25,-26,-31,-23,39,60,-21,-22,-16,-19,-18,-15,-20,-13,-14,-17,67,71,72,-24,]),'CONSTANT':([0,2,3,4,7,9,10,13,14,15,16,17,18,19,21,22,24,39,41,42,46,47,48,49,50,51,52,53,54,55,56,57,60,63,66,67,68,71,72,73,74,75,76,77,78,79,80,81,82,83,87,88,89,],[1,-27,1,-28,-30,-2,-33,-29,-31,-25,-26,-3,-31,-4,-1,-23,-32,-32,-34,-9,-5,-21,-22,-16,-19,-18,-15,-20,-13,-14,-17,1,1,1,1,-32,-24,-32,-32,-10,1,1,-8,1,1,1,1,1,1,-11,-12,-6,-7,]),'LESS':([2,4,7,13,14,15,16,17,18,19,22,43,45,46,47,48,49,50,51,52,53,54,55,56,68,],[-27,-28,-30,-29,-31,-25,-26,33,-31,33,-23,33,33,33,33,33,-16,-19,-18,-15,-20,-13,-14,-17,-24,]),'CHAR':([0,1,5,10,12,25,27,28,29,30,31,32,33,34,35,36,37,38,39,57,60,67,71,72,74,75,77,78,],[2,2,2,-33,-32,2,2,2,2,2,2,2,2,2,2,2,2,2,-32,2,2,-32,-32,-32,2,2,2,2,]),'FOREXPR':([26,],[44,]),'GREATER':([2,4,7,13,14,15,16,17,18,19,22,43,45,46,47,48,49,50,51,52,53,54,55,56,68,],[-27,-28,-30,-29,-31,-25,-26,38,-31,38,-23,38,38,38,38,38,-16,-19,-18,-15,-20,-13,-14,-17,-24,]),'TRUE':([0,1,5,10,12,25,27,28,29,30,31,32,33,34,35,36,37,38,39,57,60,67,71,72,74,75,77,78,],[4,4,4,-33,-32,4,4,4,4,4,4,4,4,4,4,4,4,4,-32,4,4,-32,-32,-32,4,4,4,4,]),'MINUS':([0,1,2,4,5,7,10,12,13,14,15,16,17,18,19,22,25,27,28,29,30,31,32,33,34,35,36,37,38,39,43,45,46,47,48,49,50,51,52,53,54,55,56,57,60,67,68,71,72,74,75,77,78,],[5,5,-27,-28,5,-30,-33,-32,-29,-31,-25,-26,37,-31,37,-23,5,5,5,5,5,5,5,5,5,5,5,5,5,-32,37,37,37,37,37,-16,37,37,-15,37,-13,-14,37,5,5,-32,-24,-32,-32,5,5,5,5,]),'DEF':([0,2,3,4,7,9,10,13,14,15,16,17,18,19,21,22,24,39,41,42,46,47,48,49,50,51,52,53,54,55,56,57,60,63,66,67,68,71,72,73,74,75,76,77,78,79,80,81,82,83,87,88,89,],[6,-27,6,-28,-30,-2,-33,-29,-31,-25,-26,-3,-31,-4,-1,-23,-32,-32,-34,-9,-5,-21,-22,-16,-19,-18,-15,-20,-13,-14,-17,6,6,6,6,-32,-24,-32,-32,-10,6,6,-8,6,6,6,6,6,6,-11,-12,-6,-7,]),'STRING':([0,1,5,10,12,25,27,28,29,30,31,32,33,34,35,36,37,38,39,57,60,67,71,72,74,75,77,78,],[7,7,7,-33,-32,7,7,7,7,7,7,7,7,7,7,7,7,7,-32,7,7,-32,-32,-32,7,7,7,7,]),'PLUS':([2,4,7,13,14,15,16,17,18,19,22,43,45,46,47,48,49,50,51,52,53,54,55,56,68,],[-27,-28,-30,-29,-31,-25,-26,36,-31,36,-23,36,36,36,36,36,-16,36,36,-15,36,-13,-14,36,-24,]),'$end':([2,3,4,7,9,13,14,15,16,17,18,19,21,22,24,41,42,46,47,48,49,50,51,52,53,54,55,56,68,73,76,83,87,88,89,],[-27,0,-28,-30,-2,-29,-31,-25,-26,-3,-31,-4,-1,-23,-32,-34,-9,-5,-21,-22,-16,-19,-18,-15,-20,-13,-14,-17,-24,-10,-8,-11,-12,-6,-7,]),'PARENR':([2,4,7,13,15,16,18,22,40,41,45,47,48,49,50,51,52,53,54,55,56,58,59,62,68,],[-27,-28,-30,-29,-25,-26,-31,-23,-32,-34,-32,-21,-22,-16,-19,-18,-15,-20,-13,-14,-17,64,65,68,-24,]),'END':([2,4,7,9,13,14,15,16,17,18,19,21,22,24,41,42,46,47,48,49,50,51,52,53,54,55,56,63,66,68,69,70,73,76,79,80,81,82,83,84,85,86,87,88,89,],[-27,-28,-30,-2,-29,-31,-25,-26,-3,-31,-4,-1,-23,-32,-34,-9,-5,-21,-22,-16,-19,-18,-15,-20,-13,-14,-17,-32,73,-24,76,-34,-10,-8,83,-32,-32,-32,-11,87,88,89,-12,-6,-7,]),'DIVIDE':([2,4,7,13,14,15,16,17,18,19,22,43,45,46,47,48,49,50,51,52,53,54,55,56,68,],[-27,-28,-30,-29,-31,-25,-26,31,-31,31,-23,31,31,31,31,31,-16,31,31,-15,31,31,31,31,-24,]),'FOR':([0,2,3,4,7,9,10,13,14,15,16,17,18,19,21,22,24,39,41,42,46,47,48,49,50,51,52,53,54,55,56,57,60,63,66,67,68,71,72,73,74,75,76,77,78,79,80,81,82,83,87,88,89,],[11,-27,11,-28,-30,-2,-33,-29,-31,-25,-26,-3,-31,-4,-1,-23,-32,-32,-34,-9,-5,-21,-22,-16,-19,-18,-15,-20,-13,-14,-17,11,11,11,11,-32,-24,-32,-32,-10,11,11,-8,11,11,11,11,11,11,-11,-12,-6,-7,]),'EQUALS':([14,20,],[28,28,]),'TIMES':([2,4,7,13,14,15,16,17,18,19,22,43,45,46,47,48,49,50,51,52,53,54,55,56,68,],[-27,-28,-30,-29,-31,-25,-26,34,-31,34,-23,34,34,34,34,34,-16,34,34,-15,34,34,34,34,-24,]),'ELSE':([2,4,7,9,13,14,15,16,17,18,19,21,22,24,41,42,46,47,48,49,50,51,52,53,54,55,56,66,68,73,76,83,87,88,89,],[-27,-28,-30,-2,-29,-31,-25,-26,-3,-31,-4,-1,-23,-32,-34,-9,-5,-21,-22,-16,-19,-18,-15,-20,-13,-14,-17,74,-24,-10,-8,-11,-12,-6,-7,]),'PARENL':([0,1,5,10,12,23,25,27,28,29,30,31,32,33,34,35,36,37,38,39,57,60,67,71,72,74,75,77,78,],[12,12,12,-33,-32,40,12,12,12,12,12,12,12,12,12,12,12,12,12,-32,12,12,-32,-32,-32,12,12,12,12,]),'IF':([0,2,3,4,7,8,9,10,13,14,15,16,17,18,19,21,22,24,39,41,42,46,47,48,49,50,51,52,53,54,55,56,57,60,63,66,67,68,70,71,72,73,74,75,76,77,78,79,80,81,82,83,87,88,89,],[-32,-27,-32,-28,-30,25,-2,-33,-29,-31,-25,-26,-3,-31,-4,-1,-23,-32,-32,-34,-9,-5,-21,-22,-16,-19,-18,-15,-20,-13,-14,-17,-32,-32,-32,-32,-32,-24,-33,-32,-32,-10,-32,-32,-8,-32,-32,-32,-32,-32,-32,-11,-12,-6,-7,]),'AND':([2,4,7,13,14,15,16,17,18,19,22,43,45,46,47,48,49,50,51,52,53,54,55,56,68,],[-27,-28,-30,-29,-31,-25,-26,29,-31,29,-23,29,29,29,-21,-22,-16,-19,-18,-15,-20,-13,-14,-17,-24,]),'FALSE':([0,1,5,10,12,25,27,28,29,30,31,32,33,34,35,36,37,38,39,57,60,67,71,72,74,75,77,78,],[13,13,13,-33,-32,13,13,13,13,13,13,13,13,13,13,13,13,13,-32,13,13,-32,-32,-32,13,13,13,13,]),'NAME':([0,1,2,3,4,5,6,7,9,10,11,12,13,14,15,16,17,18,19,21,22,24,25,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,44,46,47,48,49,50,51,52,53,54,55,56,57,60,63,66,67,68,71,72,73,74,75,76,77,78,79,80,81,82,83,87,88,89,],[14,18,-27,20,-28,18,23,-30,-2,-33,26,-32,-29,-31,-25,-26,-3,-31,-4,-1,-23,-32,18,18,18,18,18,18,18,18,18,18,18,18,18,-32,58,-34,-9,61,-5,-21,-22,-16,-19,-18,-15,-20,-13,-14,-17,14,14,20,20,-32,-24,-32,-32,-10,14,14,-8,14,14,20,20,20,20,-11,-12,-6,-7,]),'GREATEQ':([2,4,7,13,14,15,16,17,18,19,22,43,45,46,47,48,49,50,51,52,53,54,55,56,68,],[-27,-28,-30,-29,-31,-25,-26,32,-31,32,-23,32,32,32,32,32,-16,-19,-18,-15,-20,-13,-14,-17,-24,]),'INT':([0,1,5,10,12,25,27,28,29,30,31,32,33,34,35,36,37,38,39,57,60,67,71,72,74,75,77,78,],[15,15,15,-33,-32,15,15,15,15,15,15,15,15,15,15,15,15,15,-32,15,15,-32,-32,-32,15,15,15,15,]),'DOUBLE':([0,1,5,10,12,25,27,28,29,30,31,32,33,34,35,36,37,38,39,57,60,67,71,72,74,75,77,78,],[16,16,16,-33,-32,16,16,16,16,16,16,16,16,16,16,16,16,16,-32,16,16,-32,-32,-32,16,16,16,16,]),'LESSEQ':([2,4,7,13,14,15,16,17,18,19,22,43,45,46,47,48,49,50,51,52,53,54,55,56,68,],[-27,-28,-30,-29,-31,-25,-26,35,-31,35,-23,35,35,35,35,35,-16,-19,-18,-15,-20,-13,-14,-17,-24,]),'OR':([2,4,7,13,14,15,16,17,18,19,22,43,45,46,47,48,49,50,51,52,53,54,55,56,68,],[-27,-28,-30,-29,-31,-25,-26,30,-31,30,-23,30,30,30,-21,-22,-16,-19,-18,-15,-20,-13,-14,-17,-24,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statements':([0,57,60,74,75,77,78,],[3,63,66,79,80,81,82,]),'end_scope':([24,45,63,80,81,82,],[42,62,69,84,85,86,]),'new_scope':([0,3,12,39,57,60,63,66,67,71,72,74,75,77,78,79,80,81,82,],[8,8,27,57,8,8,8,8,75,77,78,8,8,8,8,8,8,8,8,]),'statement':([0,3,57,60,63,66,74,75,77,78,79,80,81,82,],[9,21,9,9,21,21,9,9,9,9,21,21,21,21,]),'if_statement':([8,],[24,]),'expression':([0,1,5,25,27,28,29,30,31,32,33,34,35,36,37,38,57,60,74,75,77,78,],[17,19,22,43,45,46,47,48,49,50,51,52,53,54,55,56,17,17,17,17,17,17,]),'empty':([0,3,12,24,39,40,45,57,60,63,66,67,71,72,74,75,77,78,79,80,81,82,],[10,10,10,41,10,59,41,10,10,70,10,10,10,10,10,10,10,10,10,70,70,70,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statements","S'",1,None,None,None),
  ('statements -> statements statement','statements',2,'p_expr','parser.py',208),
  ('statements -> statement','statements',1,'p_expr','parser.py',209),
  ('statements -> expression','statements',1,'p_expr','parser.py',210),
  ('statement -> CONSTANT expression','statement',2,'p_assign_cons','parser.py',216),
  ('statement -> NAME EQUALS expression','statement',3,'p_assign_var','parser.py',229),
  ('statement -> DEF NAME PARENL NAME PARENR DO new_scope statements end_scope END','statement',10,'p_func','parser.py',239),
  ('statement -> DEF NAME PARENL empty PARENR DO new_scope statements end_scope END','statement',10,'p_func','parser.py',240),
  ('statement -> DEF NAME DO new_scope statements end_scope END','statement',7,'p_func','parser.py',241),
  ('statement -> new_scope if_statement end_scope','statement',3,'p_if_scope','parser.py',247),
  ('if_statement -> IF expression DO statements END','if_statement',5,'p_if','parser.py',250),
  ('if_statement -> IF expression DO statements ELSE statements END','if_statement',7,'p_if','parser.py',251),
  ('statement -> FOR NAME FOREXPR NAME DO new_scope statements end_scope END','statement',9,'p_for','parser.py',260),
  ('expression -> expression PLUS expression','expression',3,'p_binary','parser.py',284),
  ('expression -> expression MINUS expression','expression',3,'p_binary','parser.py',285),
  ('expression -> expression TIMES expression','expression',3,'p_binary','parser.py',286),
  ('expression -> expression DIVIDE expression','expression',3,'p_binary','parser.py',287),
  ('expression -> expression GREATER expression','expression',3,'p_binary','parser.py',288),
  ('expression -> expression LESS expression','expression',3,'p_binary','parser.py',289),
  ('expression -> expression GREATEQ expression','expression',3,'p_binary','parser.py',290),
  ('expression -> expression LESSEQ expression','expression',3,'p_binary','parser.py',291),
  ('expression -> expression AND expression','expression',3,'p_binary','parser.py',292),
  ('expression -> expression OR expression','expression',3,'p_binary','parser.py',293),
  ('expression -> MINUS expression','expression',2,'p_minus','parser.py',354),
  ('expression -> PARENL new_scope expression end_scope PARENR','expression',5,'p_group','parser.py',360),
  ('expression -> INT','expression',1,'p_int','parser.py',366),
  ('expression -> DOUBLE','expression',1,'p_double','parser.py',372),
  ('expression -> CHAR','expression',1,'p_char','parser.py',378),
  ('expression -> TRUE','expression',1,'p_true','parser.py',384),
  ('expression -> FALSE','expression',1,'p_false','parser.py',390),
  ('expression -> STRING','expression',1,'p_string','parser.py',396),
  ('expression -> NAME','expression',1,'p_name','parser.py',407),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',427),
  ('new_scope -> empty','new_scope',1,'p_new_scope','parser.py',444),
  ('end_scope -> empty','end_scope',1,'p_end_scope','parser.py',461),
]
