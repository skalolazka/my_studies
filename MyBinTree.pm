#!/usr/bin/perl

package MyBinTree;

use strict;
#use warnings;

sub new {
    my ($class, $val) = @_;
    return bless { value => $val, left => undef, right => undef } => $class;
}

sub put_left {
    my ($self, $val) = @_;
    if (ref($val) eq 'MyBinTree') {
        $self->{left} = $val;
    }
    else {
        $self->{left} = MyBinTree->new($val);
    }
}

sub put_right {
    my ($self, $val) = @_;
    if (ref($val) eq 'MyBinTree') {
        $self->{right} = $val;
    }
    else {
        $self->{right} = MyBinTree->new($val);
    }
}

sub inorder {
    my ($class, $t, $result) = @_;
    return $result unless defined($t);
    $result = $class->inorder($t->{left}, $result);
    push(@$result, $t->{value});
    $result = $class->inorder($t->{right}, $result);
    return $result;
}

sub preorder {
    my ($class, $t, $result) = @_;
    return $result unless defined($t); 
    push(@$result, $t->{value});
    $result = $class->preorder($t->{left}, $result);
    $result = $class->preorder($t->{right}, $result);
    return $result;
}

sub postorder {
    my ($class, $t, $result) = @_;
    return $result unless defined($t); 
    $result = $class->postorder($t->{left}, $result);
    $result = $class->postorder($t->{right}, $result);
    push(@$result, $t->{value});
    return $result;
}

1;
