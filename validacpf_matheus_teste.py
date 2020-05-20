import unittest
import validacpf_matheus

class Teste_validacpf(unittest.TestCase):

    def test_retira_cpf(self):
        self.assertEqual(validacpf_matheus.retira_cpf('82736271833'), '82736271833')
        self.assertEqual(validacpf_matheus.retira_cpf('405.231.728-93'), '40523172893')
        self.assertEqual(validacpf_matheus.retira_cpf('405.231.728-9321'), '4052317289321')

    def test_valida_cpf(self):
        self.assertEqual(validacpf_matheus.valida_cpf('40523172893'), True)
        self.assertEqual(validacpf_matheus.valida_cpf('22921772101'), False)
        self.assertEqual(validacpf_matheus.valida_cpf('11111111111'), False)
        self.assertEqual(validacpf_matheus.valida_cpf('82736271833'), False)
        self.assertEqual(validacpf_matheus.valida_cpf('15232570838'), True)
        self.assertEqual(validacpf_matheus.valida_cpf('4052317289321'), False)

if __name__ == '__main__':
    unittest.main()