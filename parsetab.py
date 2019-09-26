
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftDOENDANDORIFELSEFORWHILETRUEFALSEFOREXPRNAMEleftEQUALSCONSTANTCHARINTSTRINGDOUBLENUMBERleftGREATERLESSGREATEQLESSEQleftPLUSMINUSleftTIMESDIVIDEleftLPARENRPARENrightUMINUSAND CHAR CONSTANT DEF DIVIDE DO DOUBLE ELSE END EQUALS FALSE FOR FOREXPR GREATEQ GREATER IF INT LESS LESSEQ LPAREN MINUS NAME NUMBER OR PLUS RPAREN STRING TIMES TRUE WHILEstatement : statement statement\n        | expressionstatement : NAME EQUALS expression\n                 | CONSTANT expression\n                 statement : DEF NAME LPAREN NAME RPAREN DO statement ENDstatement : IF statement DO statement END\n                 | IF statement DO statement ELSE statement ENDstatement : FOR NAME FOREXPR NAME DO statement ENDstatement : WHILE statement DO statement ENDexpression : NUMBERexpression : expression PLUS expression\n                  | expression MINUS expression\n                  | expression TIMES expression\n                  | expression DIVIDE expression\n                  expression : expression GREATER expression\n                  | expression LESS expression\n                  | expression GREATEQ expression\n                  | expression LESSEQ expression\n                  | expression AND expression\n                  | expression OR expressionexpression : MINUS expression %prec UMINUSexpression : LPAREN expression RPARENexpression : INTexpression : DOUBLEexpression : CHARexpression : TRUEexpression : FALSEexpression : STRINGexpression : NAME'
    
_lr_action_items = {'DO':([2,3,5,8,13,14,15,16,17,18,19,20,21,23,24,42,43,44,45,46,47,48,49,50,51,52,53,57,58,59,60,67,68,69,],[-10,-25,-26,-28,-27,-29,-23,-24,-2,-29,-4,38,-21,-1,40,-22,-3,-19,-20,-14,-17,-16,-13,-18,-11,-12,-15,62,-9,63,-6,-7,-8,-5,]),'CONSTANT':([0,2,3,4,5,8,9,10,13,14,15,16,17,18,19,20,21,23,24,38,40,42,43,44,45,46,47,48,49,50,51,52,53,54,56,58,60,61,62,63,64,65,66,67,68,69,],[1,-10,-25,1,-26,-28,1,1,-27,-29,-23,-24,-2,-29,-4,1,-21,1,1,1,1,-22,-3,-19,-20,-14,-17,-16,-13,-18,-11,-12,-15,1,1,-9,-6,1,1,1,1,1,1,-7,-8,-5,]),'LESS':([2,3,5,8,13,14,15,16,17,18,19,21,26,42,43,44,45,46,47,48,49,50,51,52,53,],[-10,-25,-26,-28,-27,-29,-23,-24,32,-29,32,-21,32,-22,32,32,32,-14,-17,-16,-13,-18,-11,-12,-15,]),'NUMBER':([0,1,2,3,4,5,6,8,9,10,12,13,14,15,16,17,18,19,20,21,23,24,27,28,29,30,31,32,33,34,35,36,37,38,40,42,43,44,45,46,47,48,49,50,51,52,53,54,56,58,60,61,62,63,64,65,66,67,68,69,],[2,2,-10,-25,2,-26,2,-28,2,2,2,-27,-29,-23,-24,-2,-29,-4,2,-21,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,-22,-3,-19,-20,-14,-17,-16,-13,-18,-11,-12,-15,2,2,-9,-6,2,2,2,2,2,2,-7,-8,-5,]),'CHAR':([0,1,2,3,4,5,6,8,9,10,12,13,14,15,16,17,18,19,20,21,23,24,27,28,29,30,31,32,33,34,35,36,37,38,40,42,43,44,45,46,47,48,49,50,51,52,53,54,56,58,60,61,62,63,64,65,66,67,68,69,],[3,3,-10,-25,3,-26,3,-28,3,3,3,-27,-29,-23,-24,-2,-29,-4,3,-21,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,-22,-3,-19,-20,-14,-17,-16,-13,-18,-11,-12,-15,3,3,-9,-6,3,3,3,3,3,3,-7,-8,-5,]),'WHILE':([0,2,3,4,5,8,9,10,13,14,15,16,17,18,19,20,21,23,24,38,40,42,43,44,45,46,47,48,49,50,51,52,53,54,56,58,60,61,62,63,64,65,66,67,68,69,],[4,-10,-25,4,-26,-28,4,4,-27,-29,-23,-24,-2,-29,-4,4,-21,4,4,4,4,-22,-3,-19,-20,-14,-17,-16,-13,-18,-11,-12,-15,4,4,-9,-6,4,4,4,4,4,4,-7,-8,-5,]),'FOREXPR':([25,],[41,]),'TRUE':([0,1,2,3,4,5,6,8,9,10,12,13,14,15,16,17,18,19,20,21,23,24,27,28,29,30,31,32,33,34,35,36,37,38,40,42,43,44,45,46,47,48,49,50,51,52,53,54,56,58,60,61,62,63,64,65,66,67,68,69,],[5,5,-10,-25,5,-26,5,-28,5,5,5,-27,-29,-23,-24,-2,-29,-4,5,-21,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,-22,-3,-19,-20,-14,-17,-16,-13,-18,-11,-12,-15,5,5,-9,-6,5,5,5,5,5,5,-7,-8,-5,]),'MINUS':([0,1,2,3,4,5,6,8,9,10,12,13,14,15,16,17,18,19,20,21,23,24,26,27,28,29,30,31,32,33,34,35,36,37,38,40,42,43,44,45,46,47,48,49,50,51,52,53,54,56,58,60,61,62,63,64,65,66,67,68,69,],[6,6,-10,-25,6,-26,6,-28,6,6,6,-27,-29,-23,-24,36,-29,36,6,-21,6,6,36,6,6,6,6,6,6,6,6,6,6,6,6,6,-22,36,36,36,-14,36,36,-13,36,-11,-12,36,6,6,-9,-6,6,6,6,6,6,6,-7,-8,-5,]),'DEF':([0,2,3,4,5,8,9,10,13,14,15,16,17,18,19,20,21,23,24,38,40,42,43,44,45,46,47,48,49,50,51,52,53,54,56,58,60,61,62,63,64,65,66,67,68,69,],[7,-10,-25,7,-26,-28,7,7,-27,-29,-23,-24,-2,-29,-4,7,-21,7,7,7,7,-22,-3,-19,-20,-14,-17,-16,-13,-18,-11,-12,-15,7,7,-9,-6,7,7,7,7,7,7,-7,-8,-5,]),'DIVIDE':([2,3,5,8,13,14,15,16,17,18,19,21,26,42,43,44,45,46,47,48,49,50,51,52,53,],[-10,-25,-26,-28,-27,-29,-23,-24,30,-29,30,-21,30,-22,30,30,30,-14,30,30,-13,30,30,30,30,]),'RPAREN':([2,3,5,8,13,15,16,18,21,26,42,44,45,46,47,48,49,50,51,52,53,55,],[-10,-25,-26,-28,-27,-23,-24,-29,-21,42,-22,-19,-20,-14,-17,-16,-13,-18,-11,-12,-15,59,]),'PLUS':([2,3,5,8,13,14,15,16,17,18,19,21,26,42,43,44,45,46,47,48,49,50,51,52,53,],[-10,-25,-26,-28,-27,-29,-23,-24,35,-29,35,-21,35,-22,35,35,35,-14,35,35,-13,35,-11,-12,35,]),'IF':([0,2,3,4,5,8,9,10,13,14,15,16,17,18,19,20,21,23,24,38,40,42,43,44,45,46,47,48,49,50,51,52,53,54,56,58,60,61,62,63,64,65,66,67,68,69,],[10,-10,-25,10,-26,-28,10,10,-27,-29,-23,-24,-2,-29,-4,10,-21,10,10,10,10,-22,-3,-19,-20,-14,-17,-16,-13,-18,-11,-12,-15,10,10,-9,-6,10,10,10,10,10,10,-7,-8,-5,]),'$end':([2,3,5,8,9,13,14,15,16,17,18,19,21,23,42,43,44,45,46,47,48,49,50,51,52,53,58,60,67,68,69,],[-10,-25,-26,-28,0,-27,-29,-23,-24,-2,-29,-4,-21,-1,-22,-3,-19,-20,-14,-17,-16,-13,-18,-11,-12,-15,-9,-6,-7,-8,-5,]),'END':([2,3,5,8,13,14,15,16,17,18,19,21,23,42,43,44,45,46,47,48,49,50,51,52,53,54,56,58,60,64,65,66,67,68,69,],[-10,-25,-26,-28,-27,-29,-23,-24,-2,-29,-4,-21,-1,-22,-3,-19,-20,-14,-17,-16,-13,-18,-11,-12,-15,58,60,-9,-6,67,68,69,-7,-8,-5,]),'STRING':([0,1,2,3,4,5,6,8,9,10,12,13,14,15,16,17,18,19,20,21,23,24,27,28,29,30,31,32,33,34,35,36,37,38,40,42,43,44,45,46,47,48,49,50,51,52,53,54,56,58,60,61,62,63,64,65,66,67,68,69,],[8,8,-10,-25,8,-26,8,-28,8,8,8,-27,-29,-23,-24,-2,-29,-4,8,-21,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,-22,-3,-19,-20,-14,-17,-16,-13,-18,-11,-12,-15,8,8,-9,-6,8,8,8,8,8,8,-7,-8,-5,]),'FOR':([0,2,3,4,5,8,9,10,13,14,15,16,17,18,19,20,21,23,24,38,40,42,43,44,45,46,47,48,49,50,51,52,53,54,56,58,60,61,62,63,64,65,66,67,68,69,],[11,-10,-25,11,-26,-28,11,11,-27,-29,-23,-24,-2,-29,-4,11,-21,11,11,11,11,-22,-3,-19,-20,-14,-17,-16,-13,-18,-11,-12,-15,11,11,-9,-6,11,11,11,11,11,11,-7,-8,-5,]),'EQUALS':([14,],[27,]),'TIMES':([2,3,5,8,13,14,15,16,17,18,19,21,26,42,43,44,45,46,47,48,49,50,51,52,53,],[-10,-25,-26,-28,-27,-29,-23,-24,33,-29,33,-21,33,-22,33,33,33,-14,33,33,-13,33,33,33,33,]),'LPAREN':([0,1,2,3,4,5,6,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,27,28,29,30,31,32,33,34,35,36,37,38,40,42,43,44,45,46,47,48,49,50,51,52,53,54,56,58,60,61,62,63,64,65,66,67,68,69,],[12,12,-10,-25,12,-26,12,-28,12,12,12,-27,-29,-23,-24,-2,-29,-4,12,-21,39,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,-22,-3,-19,-20,-14,-17,-16,-13,-18,-11,-12,-15,12,12,-9,-6,12,12,12,12,12,12,-7,-8,-5,]),'ELSE':([2,3,5,8,13,14,15,16,17,18,19,21,23,42,43,44,45,46,47,48,49,50,51,52,53,56,58,60,67,68,69,],[-10,-25,-26,-28,-27,-29,-23,-24,-2,-29,-4,-21,-1,-22,-3,-19,-20,-14,-17,-16,-13,-18,-11,-12,-15,61,-9,-6,-7,-8,-5,]),'GREATER':([2,3,5,8,13,14,15,16,17,18,19,21,26,42,43,44,45,46,47,48,49,50,51,52,53,],[-10,-25,-26,-28,-27,-29,-23,-24,37,-29,37,-21,37,-22,37,37,37,-14,-17,-16,-13,-18,-11,-12,-15,]),'AND':([2,3,5,8,13,14,15,16,17,18,19,21,26,42,43,44,45,46,47,48,49,50,51,52,53,],[-10,-25,-26,-28,-27,-29,-23,-24,28,-29,28,-21,28,-22,28,-19,-20,-14,-17,-16,-13,-18,-11,-12,-15,]),'FALSE':([0,1,2,3,4,5,6,8,9,10,12,13,14,15,16,17,18,19,20,21,23,24,27,28,29,30,31,32,33,34,35,36,37,38,40,42,43,44,45,46,47,48,49,50,51,52,53,54,56,58,60,61,62,63,64,65,66,67,68,69,],[13,13,-10,-25,13,-26,13,-28,13,13,13,-27,-29,-23,-24,-2,-29,-4,13,-21,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,-22,-3,-19,-20,-14,-17,-16,-13,-18,-11,-12,-15,13,13,-9,-6,13,13,13,13,13,13,-7,-8,-5,]),'NAME':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,56,58,60,61,62,63,64,65,66,67,68,69,],[14,18,-10,-25,14,-26,18,22,-28,14,14,25,18,-27,-29,-23,-24,-2,-29,-4,14,-21,14,14,18,18,18,18,18,18,18,18,18,18,18,14,55,14,57,-22,-3,-19,-20,-14,-17,-16,-13,-18,-11,-12,-15,14,14,-9,-6,14,14,14,14,14,14,-7,-8,-5,]),'GREATEQ':([2,3,5,8,13,14,15,16,17,18,19,21,26,42,43,44,45,46,47,48,49,50,51,52,53,],[-10,-25,-26,-28,-27,-29,-23,-24,31,-29,31,-21,31,-22,31,31,31,-14,-17,-16,-13,-18,-11,-12,-15,]),'INT':([0,1,2,3,4,5,6,8,9,10,12,13,14,15,16,17,18,19,20,21,23,24,27,28,29,30,31,32,33,34,35,36,37,38,40,42,43,44,45,46,47,48,49,50,51,52,53,54,56,58,60,61,62,63,64,65,66,67,68,69,],[15,15,-10,-25,15,-26,15,-28,15,15,15,-27,-29,-23,-24,-2,-29,-4,15,-21,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,-22,-3,-19,-20,-14,-17,-16,-13,-18,-11,-12,-15,15,15,-9,-6,15,15,15,15,15,15,-7,-8,-5,]),'DOUBLE':([0,1,2,3,4,5,6,8,9,10,12,13,14,15,16,17,18,19,20,21,23,24,27,28,29,30,31,32,33,34,35,36,37,38,40,42,43,44,45,46,47,48,49,50,51,52,53,54,56,58,60,61,62,63,64,65,66,67,68,69,],[16,16,-10,-25,16,-26,16,-28,16,16,16,-27,-29,-23,-24,-2,-29,-4,16,-21,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,-22,-3,-19,-20,-14,-17,-16,-13,-18,-11,-12,-15,16,16,-9,-6,16,16,16,16,16,16,-7,-8,-5,]),'LESSEQ':([2,3,5,8,13,14,15,16,17,18,19,21,26,42,43,44,45,46,47,48,49,50,51,52,53,],[-10,-25,-26,-28,-27,-29,-23,-24,34,-29,34,-21,34,-22,34,34,34,-14,-17,-16,-13,-18,-11,-12,-15,]),'OR':([2,3,5,8,13,14,15,16,17,18,19,21,26,42,43,44,45,46,47,48,49,50,51,52,53,],[-10,-25,-26,-28,-27,-29,-23,-24,29,-29,29,-21,29,-22,29,-19,-20,-14,-17,-16,-13,-18,-11,-12,-15,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,1,4,6,9,10,12,20,23,24,27,28,29,30,31,32,33,34,35,36,37,38,40,54,56,61,62,63,64,65,66,],[17,19,17,21,17,17,26,17,17,17,43,44,45,46,47,48,49,50,51,52,53,17,17,17,17,17,17,17,17,17,17,]),'statement':([0,4,9,10,20,23,24,38,40,54,56,61,62,63,64,65,66,],[9,20,23,24,23,23,23,54,56,23,23,64,65,66,23,23,23,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> statement statement','statement',2,'p_expr','parser.py',228),
  ('statement -> expression','statement',1,'p_expr','parser.py',229),
  ('statement -> NAME EQUALS expression','statement',3,'p_assign','parser.py',233),
  ('statement -> CONSTANT expression','statement',2,'p_assign','parser.py',234),
  ('statement -> DEF NAME LPAREN NAME RPAREN DO statement END','statement',8,'p_func','parser.py',239),
  ('statement -> IF statement DO statement END','statement',5,'p_if','parser.py',243),
  ('statement -> IF statement DO statement ELSE statement END','statement',7,'p_if','parser.py',244),
  ('statement -> FOR NAME FOREXPR NAME DO statement END','statement',7,'p_for','parser.py',248),
  ('statement -> WHILE statement DO statement END','statement',5,'p_while','parser.py',252),
  ('expression -> NUMBER','expression',1,'p_number','parser.py',256),
  ('expression -> expression PLUS expression','expression',3,'p_binary','parser.py',260),
  ('expression -> expression MINUS expression','expression',3,'p_binary','parser.py',261),
  ('expression -> expression TIMES expression','expression',3,'p_binary','parser.py',262),
  ('expression -> expression DIVIDE expression','expression',3,'p_binary','parser.py',263),
  ('expression -> expression GREATER expression','expression',3,'p_comparison','parser.py',268),
  ('expression -> expression LESS expression','expression',3,'p_comparison','parser.py',269),
  ('expression -> expression GREATEQ expression','expression',3,'p_comparison','parser.py',270),
  ('expression -> expression LESSEQ expression','expression',3,'p_comparison','parser.py',271),
  ('expression -> expression AND expression','expression',3,'p_comparison','parser.py',272),
  ('expression -> expression OR expression','expression',3,'p_comparison','parser.py',273),
  ('expression -> MINUS expression','expression',2,'p_minus','parser.py',277),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_group','parser.py',281),
  ('expression -> INT','expression',1,'p_int','parser.py',285),
  ('expression -> DOUBLE','expression',1,'p_double','parser.py',289),
  ('expression -> CHAR','expression',1,'p_char','parser.py',293),
  ('expression -> TRUE','expression',1,'p_true','parser.py',297),
  ('expression -> FALSE','expression',1,'p_false','parser.py',301),
  ('expression -> STRING','expression',1,'p_string','parser.py',305),
  ('expression -> NAME','expression',1,'p_name','parser.py',309),
]
