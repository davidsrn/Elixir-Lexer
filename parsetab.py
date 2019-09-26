
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftDOENDANDORIFELSEFORWHILETRUEFALSEFOREXPRNAMEleftEQUALSCONSTANTCHARINTSTRINGDOUBLEleftGREATERLESSGREATEQLESSEQleftPLUSMINUSleftTIMESDIVIDEleftPARENLPARENRrightUMINUSAND CHAR CONSTANT DEF DIVIDE DO DOUBLE ELSE END EQUALS FALSE FOR FOREXPR GREATEQ GREATER IF INT LESS LESSEQ MINUS NAME OR PARENL PARENR PLUS STRING TIMES TRUE WHILEstatements : statements statement\n        | statement\n        | expressionstatement : NAME EQUALS expression\n                 | CONSTANT expression\n                 statement : DEF NAME PARENL NAME PARENR DO statements ENDstatement : IF expression DO statements END\n                 | IF expression DO statements ELSE statements END\n                 statement : FOR NAME FOREXPR NAME DO statements ENDstatement : WHILE expression DO statements ENDexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression TIMES expression\n                  | expression DIVIDE expression\n                  expression : expression GREATER expression\n                  | expression LESS expression\n                  | expression GREATEQ expression\n                  | expression LESSEQ expression\n                  | expression AND expression\n                  | expression OR expressionexpression : MINUS expression %prec UMINUSexpression : PARENL expression PARENRexpression : INTexpression : DOUBLEexpression : CHARexpression : TRUEexpression : FALSEexpression : STRINGexpression : NAME'
    
_lr_action_items = {'DO':([2,5,8,13,15,16,18,20,23,25,43,45,46,47,48,49,50,51,52,53,54,58,60,],[-25,-26,-28,-27,-23,-24,-29,39,-21,41,-22,-19,-20,-14,-17,-16,-13,-18,-11,-12,-15,63,64,]),'CONSTANT':([0,2,4,5,8,9,13,14,15,16,17,18,19,22,23,39,41,43,44,45,46,47,48,49,50,51,52,53,54,55,57,59,61,62,63,64,65,66,67,68,69,70,],[1,-25,1,-26,-28,-2,-27,-29,-23,-24,-3,-29,-5,-1,-21,1,1,-22,-4,-19,-20,-14,-17,-16,-13,-18,-11,-12,-15,1,1,-10,-7,1,1,1,1,1,1,-8,-9,-6,]),'LESS':([2,5,8,13,14,15,16,17,18,19,20,23,25,27,43,44,45,46,47,48,49,50,51,52,53,54,],[-25,-26,-28,-27,-29,-23,-24,33,-29,33,33,-21,33,33,-22,33,33,33,-14,-17,-16,-13,-18,-11,-12,-15,]),'CHAR':([0,1,3,6,10,12,28,29,30,31,32,33,34,35,36,37,38,39,41,62,63,64,],[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,]),'WHILE':([0,2,4,5,8,9,13,14,15,16,17,18,19,22,23,39,41,43,44,45,46,47,48,49,50,51,52,53,54,55,57,59,61,62,63,64,65,66,67,68,69,70,],[3,-25,3,-26,-28,-2,-27,-29,-23,-24,-3,-29,-5,-1,-21,3,3,-22,-4,-19,-20,-14,-17,-16,-13,-18,-11,-12,-15,3,3,-10,-7,3,3,3,3,3,3,-8,-9,-6,]),'FOREXPR':([26,],[42,]),'GREATER':([2,5,8,13,14,15,16,17,18,19,20,23,25,27,43,44,45,46,47,48,49,50,51,52,53,54,],[-25,-26,-28,-27,-29,-23,-24,38,-29,38,38,-21,38,38,-22,38,38,38,-14,-17,-16,-13,-18,-11,-12,-15,]),'TRUE':([0,1,3,6,10,12,28,29,30,31,32,33,34,35,36,37,38,39,41,62,63,64,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'MINUS':([0,1,2,3,5,6,8,10,12,13,14,15,16,17,18,19,20,23,25,27,28,29,30,31,32,33,34,35,36,37,38,39,41,43,44,45,46,47,48,49,50,51,52,53,54,62,63,64,],[6,6,-25,6,-26,6,-28,6,6,-27,-29,-23,-24,37,-29,37,37,-21,37,37,6,6,6,6,6,6,6,6,6,6,6,6,6,-22,37,37,37,-14,37,37,-13,37,-11,-12,37,6,6,6,]),'DEF':([0,2,4,5,8,9,13,14,15,16,17,18,19,22,23,39,41,43,44,45,46,47,48,49,50,51,52,53,54,55,57,59,61,62,63,64,65,66,67,68,69,70,],[7,-25,7,-26,-28,-2,-27,-29,-23,-24,-3,-29,-5,-1,-21,7,7,-22,-4,-19,-20,-14,-17,-16,-13,-18,-11,-12,-15,7,7,-10,-7,7,7,7,7,7,7,-8,-9,-6,]),'STRING':([0,1,3,6,10,12,28,29,30,31,32,33,34,35,36,37,38,39,41,62,63,64,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'PLUS':([2,5,8,13,14,15,16,17,18,19,20,23,25,27,43,44,45,46,47,48,49,50,51,52,53,54,],[-25,-26,-28,-27,-29,-23,-24,36,-29,36,36,-21,36,36,-22,36,36,36,-14,36,36,-13,36,-11,-12,36,]),'$end':([2,4,5,8,9,13,14,15,16,17,18,19,22,23,43,44,45,46,47,48,49,50,51,52,53,54,59,61,68,69,70,],[-25,0,-26,-28,-2,-27,-29,-23,-24,-3,-29,-5,-1,-21,-22,-4,-19,-20,-14,-17,-16,-13,-18,-11,-12,-15,-10,-7,-8,-9,-6,]),'PARENR':([2,5,8,13,15,16,18,23,27,43,45,46,47,48,49,50,51,52,53,54,56,],[-25,-26,-28,-27,-23,-24,-29,-21,43,-22,-19,-20,-14,-17,-16,-13,-18,-11,-12,-15,60,]),'END':([2,5,8,9,13,14,15,16,17,18,19,22,23,43,44,45,46,47,48,49,50,51,52,53,54,55,57,59,61,65,66,67,68,69,70,],[-25,-26,-28,-2,-27,-29,-23,-24,-3,-29,-5,-1,-21,-22,-4,-19,-20,-14,-17,-16,-13,-18,-11,-12,-15,59,61,-10,-7,68,69,70,-8,-9,-6,]),'DIVIDE':([2,5,8,13,14,15,16,17,18,19,20,23,25,27,43,44,45,46,47,48,49,50,51,52,53,54,],[-25,-26,-28,-27,-29,-23,-24,31,-29,31,31,-21,31,31,-22,31,31,31,-14,31,31,-13,31,31,31,31,]),'FOR':([0,2,4,5,8,9,13,14,15,16,17,18,19,22,23,39,41,43,44,45,46,47,48,49,50,51,52,53,54,55,57,59,61,62,63,64,65,66,67,68,69,70,],[11,-25,11,-26,-28,-2,-27,-29,-23,-24,-3,-29,-5,-1,-21,11,11,-22,-4,-19,-20,-14,-17,-16,-13,-18,-11,-12,-15,11,11,-10,-7,11,11,11,11,11,11,-8,-9,-6,]),'EQUALS':([14,21,],[28,28,]),'ELSE':([2,5,8,9,13,14,15,16,17,18,19,22,23,43,44,45,46,47,48,49,50,51,52,53,54,57,59,61,68,69,70,],[-25,-26,-28,-2,-27,-29,-23,-24,-3,-29,-5,-1,-21,-22,-4,-19,-20,-14,-17,-16,-13,-18,-11,-12,-15,62,-10,-7,-8,-9,-6,]),'TIMES':([2,5,8,13,14,15,16,17,18,19,20,23,25,27,43,44,45,46,47,48,49,50,51,52,53,54,],[-25,-26,-28,-27,-29,-23,-24,34,-29,34,34,-21,34,34,-22,34,34,34,-14,34,34,-13,34,34,34,34,]),'PARENL':([0,1,3,6,10,12,24,28,29,30,31,32,33,34,35,36,37,38,39,41,62,63,64,],[12,12,12,12,12,12,40,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'IF':([0,2,4,5,8,9,13,14,15,16,17,18,19,22,23,39,41,43,44,45,46,47,48,49,50,51,52,53,54,55,57,59,61,62,63,64,65,66,67,68,69,70,],[10,-25,10,-26,-28,-2,-27,-29,-23,-24,-3,-29,-5,-1,-21,10,10,-22,-4,-19,-20,-14,-17,-16,-13,-18,-11,-12,-15,10,10,-10,-7,10,10,10,10,10,10,-8,-9,-6,]),'AND':([2,5,8,13,14,15,16,17,18,19,20,23,25,27,43,44,45,46,47,48,49,50,51,52,53,54,],[-25,-26,-28,-27,-29,-23,-24,29,-29,29,29,-21,29,29,-22,29,-19,-20,-14,-17,-16,-13,-18,-11,-12,-15,]),'FALSE':([0,1,3,6,10,12,28,29,30,31,32,33,34,35,36,37,38,39,41,62,63,64,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'NAME':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,22,23,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,57,59,61,62,63,64,65,66,67,68,69,70,],[14,18,-25,18,21,-26,18,24,-28,-2,18,26,18,-27,-29,-23,-24,-3,-29,-5,-1,-21,18,18,18,18,18,18,18,18,18,18,18,14,56,14,58,-22,-4,-19,-20,-14,-17,-16,-13,-18,-11,-12,-15,21,21,-10,-7,14,14,14,21,21,21,-8,-9,-6,]),'GREATEQ':([2,5,8,13,14,15,16,17,18,19,20,23,25,27,43,44,45,46,47,48,49,50,51,52,53,54,],[-25,-26,-28,-27,-29,-23,-24,32,-29,32,32,-21,32,32,-22,32,32,32,-14,-17,-16,-13,-18,-11,-12,-15,]),'INT':([0,1,3,6,10,12,28,29,30,31,32,33,34,35,36,37,38,39,41,62,63,64,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'DOUBLE':([0,1,3,6,10,12,28,29,30,31,32,33,34,35,36,37,38,39,41,62,63,64,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'LESSEQ':([2,5,8,13,14,15,16,17,18,19,20,23,25,27,43,44,45,46,47,48,49,50,51,52,53,54,],[-25,-26,-28,-27,-29,-23,-24,35,-29,35,35,-21,35,35,-22,35,35,35,-14,-17,-16,-13,-18,-11,-12,-15,]),'OR':([2,5,8,13,14,15,16,17,18,19,20,23,25,27,43,44,45,46,47,48,49,50,51,52,53,54,],[-25,-26,-28,-27,-29,-23,-24,30,-29,30,30,-21,30,30,-22,30,-19,-20,-14,-17,-16,-13,-18,-11,-12,-15,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,1,3,6,10,12,28,29,30,31,32,33,34,35,36,37,38,39,41,62,63,64,],[17,19,20,23,25,27,44,45,46,47,48,49,50,51,52,53,54,17,17,17,17,17,]),'statements':([0,39,41,62,63,64,],[4,55,57,65,66,67,]),'statement':([0,4,39,41,55,57,62,63,64,65,66,67,],[9,22,9,9,22,22,9,9,9,22,22,22,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statements","S'",1,None,None,None),
  ('statements -> statements statement','statements',2,'p_expr','parser.py',149),
  ('statements -> statement','statements',1,'p_expr','parser.py',150),
  ('statements -> expression','statements',1,'p_expr','parser.py',151),
  ('statement -> NAME EQUALS expression','statement',3,'p_assign','parser.py',155),
  ('statement -> CONSTANT expression','statement',2,'p_assign','parser.py',156),
  ('statement -> DEF NAME PARENL NAME PARENR DO statements END','statement',8,'p_func','parser.py',161),
  ('statement -> IF expression DO statements END','statement',5,'p_if','parser.py',165),
  ('statement -> IF expression DO statements ELSE statements END','statement',7,'p_if','parser.py',166),
  ('statement -> FOR NAME FOREXPR NAME DO statements END','statement',7,'p_for','parser.py',171),
  ('statement -> WHILE expression DO statements END','statement',5,'p_while','parser.py',175),
  ('expression -> expression PLUS expression','expression',3,'p_binary','parser.py',192),
  ('expression -> expression MINUS expression','expression',3,'p_binary','parser.py',193),
  ('expression -> expression TIMES expression','expression',3,'p_binary','parser.py',194),
  ('expression -> expression DIVIDE expression','expression',3,'p_binary','parser.py',195),
  ('expression -> expression GREATER expression','expression',3,'p_comparison','parser.py',200),
  ('expression -> expression LESS expression','expression',3,'p_comparison','parser.py',201),
  ('expression -> expression GREATEQ expression','expression',3,'p_comparison','parser.py',202),
  ('expression -> expression LESSEQ expression','expression',3,'p_comparison','parser.py',203),
  ('expression -> expression AND expression','expression',3,'p_comparison','parser.py',204),
  ('expression -> expression OR expression','expression',3,'p_comparison','parser.py',205),
  ('expression -> MINUS expression','expression',2,'p_minus','parser.py',209),
  ('expression -> PARENL expression PARENR','expression',3,'p_group','parser.py',213),
  ('expression -> INT','expression',1,'p_int','parser.py',217),
  ('expression -> DOUBLE','expression',1,'p_double','parser.py',221),
  ('expression -> CHAR','expression',1,'p_char','parser.py',225),
  ('expression -> TRUE','expression',1,'p_true','parser.py',229),
  ('expression -> FALSE','expression',1,'p_false','parser.py',233),
  ('expression -> STRING','expression',1,'p_string','parser.py',237),
  ('expression -> NAME','expression',1,'p_name','parser.py',241),
]
