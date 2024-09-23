from rest_framework.serializers import ModelSerializer
from core.models import Livro, Formapagamento, User


class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"


class FormapagamentoSerializer(ModelSerializer):
    class Meta:
        model = Formapagamento
        fields = "__all__"


class RegisterUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "first_name",
            "username", 
            "password", 
            "email", 
            "endereco", 
            "numero", 
            "cep", 
            "complemento",
            "celular",
            "bairro",
            "cidade",
            "estado"
        ]
    def create(self, validated_data):
        user = User.objects.create_user(
            first_name=validated_data['first_name'],
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            endereco=validated_data['endereco'],
            numero=validated_data['numero'],
            cep=validated_data['cep'],
            complemento=validated_data['complemento'],
            celular=validated_data['celular'],
            bairro=validated_data['bairro'],
            cidade=validated_data['cidade'],
            estado=validated_data['estado']
        )
        return user
        
